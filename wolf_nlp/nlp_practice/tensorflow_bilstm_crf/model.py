#coding=utf-8

import os
import sys
import time
import numpy as np
import tensorflow as tf
from tensorflow.train import AdamOptimizer, AdagradOptimizer, AdadeltaOptimizer, RMSPropOptimizer, MomentumOptimizer, GradientDescentOptimizer
from tensorflow.contrib import rnn
from tensorflow.contrib import crf
from tensorflow.contrib.layers import xavier_initializer
from text_handler import batch_generator, tag2label, pad_sequences

class BiLSTM_CRF(object):
    def __init__(self, batch_size, epoch, hidden_size, embeddings, crf, update_embedding, dropout_keepprob, optimizer, learning_rate, clip, tag2label, vocab, shuffle, paths, config):
        self.batch_size_ = batch_size
        self.epoch_ = epoch
        self.hidden_size_ = hidden_size
        self.embeddings_ = embeddings
        self.crf_ = crf
        self.update_embedding_ = update_embedding
        self.dropout_keepprob_ = dropout_keepprob
        self.optimizer_ = optimizer
        self.learning_rate_ = learning_rate
        self.clip_grad_ = clip
        self.tag2label_ = tag2label
        self.num_tags_ = len(tag2label)
        self.vocab_ = vocab
        self.shuffle_ = shuffle
        self.model_path_ = paths
        self.summary_path_ = paths
        self.result_path_ = paths
        self.config_ = config
        self.init_global_variables_ = None

    def build_graph(self):
        self.init_variables()
        self.lookup_layer()
        self.bilstm_layer()
        self.softmax_prediction_optimizer()
        self.loss_optimizer()
        self.train_optimizer()
        self.init_global_variables_ = tf.global_variables_initializer()

    def init_variables(self):
        self.word_ids_ = tf.placeholder(tf.int32, shape=[None, None], name='word_ids_')
        self.labels_ = tf.placeholder(tf.int32, shape=[None, None], name='labels_')
        self.sequence_length_ = tf.placeholder(tf.int32, shape=[None,], name='sequence_length_')
        self.dropout_ph_ = tf.placeholder(tf.float32, shape=[], name='dropout_ph_')
        self.learning_rate_ph_ = tf.placeholder(tf.float32, shape=[], name='learning_rate_ph_')

    def lookup_layer(self):
        with tf.variable_scope('words'):
            _word_embeddings = tf.Variable(self.embeddings_, dtype=tf.float32, trainable=self.update_embedding_, name='_word_embeddings')
            word_embeddings = tf.nn.embedding_lookup(params=_word_embeddings, ids=self.word_ids_, name='word_embeddings')
        self.word_embeddings_ = tf.nn.dropout(word_embeddings, self.dropout_ph_)

    def bilstm_layer(self):
        with tf.variable_scope('bi-lstm'):
            cell_fw = rnn.BasicLSTMCell(self.hidden_size_)
            cell_bw = rnn.BasicLSTMCell(self.hidden_size_)
            output_fw_seq, output_bw_seq, _ = tf.nn.bidirectional_dynamic_rnn(cell_fw=cell_fw, cell_bw=cell_bw, inputs=self.word_embeddings_, sequence_length=self.sequence_length_,dtype=tf.float32)
            output = tf.concat([output_fw_seq, output_bw_seq], axis=-1)
            output = tf.nn.dropout(output, self.dropout_ph_)

        with tf.variable_scope('proj'):
            W = tf.get_variable(shape=[2 * self.hidden_size_, self.num_tags_], initializer=xavier_initializer, dtype=tf.float32, name='W')
            b = tf.get_variable(shape=[self.num_tags_], initializer=tf.zeros_initializer(), name='b')
            s = tf.shape(output)
            output = tf.reshape(output, [-1, 2*self.hidden_size_])
            prediction = tf.matmul(output, W) + b
            self.logits_ = tf.reshape(prediction, [-1, s[1], self.num_tags_])


    def loss_optimizer(self):
        if self.crf_:
            log_likelihood,self.transition_params_ = crf_log_likelihood(inputs=self.logits_, tag_indices=self.labels_, sequence_lengths=self.sequence_length_)
            self.loss_ = -tf.reduce_mean(log_likelihood)
        else:
            losses = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.logits_, labels=self.labels_)
            mask = tf.sequence_mask(self.sequence_length_)
            losses = tf.boolean_mask(losses, mask=mask)
            self.loss_ = tf.reduce_mean(losses)
        tf.summary.scalar('loss', self.loss_)

    def softmax_prediction_optimizer(self):
        if not self.crf_:
            self.labels_softmax_ = tf.argmax(self.logits_, axis=-1)
            self.labels_softmax_ = tf.cast(self.labels_softmax_, tf.int32)

    def train_optimizer(self):
        with tf.variable_scope('train_step'):
            self.global_step_ = tf.Variable(0, name='global_step_', trainable=False)
            if self.optimizer_ == 'Adam':
                opt = AdamOptimizer(learning_rate=self.learning_rate_ph_)
            elif self.optimizer_ == 'Adagrad':
                opt = AdagradOptimizer(learning_rate=self.learning_rate_ph_)
            elif self.optimizer_ == 'Adadelta':
                opt = AdadeltaOptimizer(learning_rate=self.learning_rate_ph_)
            elif self.optimizer_ == 'RMSProp':
                opt = RMSPropOptimizer(learning_rate=self.learning_rate_ph_)
            elif self.optimizer_ == 'Momentum':
                opt = MomentumOptimizer(learning_rate=self.learning_rate_ph_, momentum=0.9)
            else:
                opt = GradientDescentOptimizer(learning_rate=self.learning_rate_ph_)

            """"
            #修正梯度参数的另一种写法
            #获取全部可以训练的参数tf_variables
            tf_variables = tf.trainable_variables()
            #提前计算梯度
            tf_grads = tf.gradients(self.loss_, tf_variables)
            #由它们的范数之和之比求多个张量的值
            tf_grads,_ = tf.clip_by_global_norm(tf_grads, self.clip_grad_)
            #将前面clip过的梯度应用到可训练的参数上
            self.train_optimizer_ = opt.apply_gradients(zip(tf_grads, tf_variables))
            """"

            # 获取参数，提前计算梯度
            grads_and_vars = opt.compute_gradients(self.loss_)
            # 修正梯度值
            grads_and_vars_clip = [[tf.clip_by_value(g, -self.clip_grad_, self.clip_grad_), v] for g,v in grads_and_vars]
            # 应用修正后的梯度值
            self.train_optimizer_ = opt.apply_gradients(grads_and_vars_clip, global_step=self.global_step_)

    def add_summary(self, sess):
        self.merged_ = tf.summary.merge_all()
        self.file_writer_ = tf.summary.FileWriter(self.summary_path_, sess.graph)

    def train(self, train, dev):
        train_saver = tf.train.Saver(tf.global_variables())
        with tf.Session(config=self.config_) as sess:
            sess.run(self.init_global_variables_)
            sess.add_summary(sess)

            for epoch in range(self.epoch_):
                self.run_one_epoch(sess, train, dev, tag2label, epoch, train_saver)

    def test(self):
        pass
    def demo_one(self):
        pass
    def run_one_epoch(self, sess, train, dev, tag2label, epoch, saver):
        num_batches = (len(train) + self.batch_size_ - 1) // self.batch_size_
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        one_batch = batch_generator(train, self.batch_size, self.vocab_, tag2label, shuffle=self.shuffle_)
        for step,(seqs,labels) in enumerate(one_batch):
            print('handle {0} batch {1} batches'.format(step+1, num_batches))
            step_num = epoch * num_batches + step + 1
            feed_dict, _ = self.get_feed_dict(seqs, labels, self.learning_rate_, self.dropout_keepprob_)
            run_ops = [self.train_optimizer_, self.loss_, self.merged_, self.global_step_]
            _, loss_train, summary, step_num_ = sess.run(run_ops, feed_dict=feed_dict)
            if (step+1 == 1) or \
                (step + 1) % 300 == 0 or \
                step + 1 == num_batches:
                print('{0} epoch {1}, step {2}, loss {3:.4}, global_step {4}'.format(start_time, epoch+1, step+1, loss_train, step_num))
            #这里设置的step_num是否有问题?
            self.file_writer_.add_summary(summary, step_num)
            #global_step设置是否有问题
            if step + 1 == num_batches:
                saver.save(sess, self.model_path_, global_step=step_num)
        print('validation / test')
        


    def get_feed_dict(self, seqs, labels=None, learning_rate=None, dropout=None):
        word_ids,seq_len_list = pad_sequences(seqs)
        feed_dict = {self.word_ids_:word_ids,
                    self.sequence_length_:seq_len_list}
        if labels is not None:
            lbs,_ = pad_sequences(labels)
            feed_dict[self.labels_] = lbs
        if learning_rate is not None:
            feed_dict[self.learning_rate_ph_] = learning_rate
        if dropout is not None:
            feed_dict[self.dropout_ph_] = dropout
        return feed_dict,seq_len_list

    def dev_one_epoch(self):
        pass
    def prediction_one_batch(self):
        pass
    def evaluate(self):
        pass