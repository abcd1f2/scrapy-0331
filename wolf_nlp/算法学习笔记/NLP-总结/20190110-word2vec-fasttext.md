## NLP_总结 -- word2vec vs fasttext
- **概述：**
>       腾讯的800W的词向量就是通过 Directional Skip-Gram 训练得到的
>
>
>       word2vec相对于DNN有连个改进：
>           1、输入层到隐藏层的映射
>               没有采取神经网络的线性变换加激活函数的方法，而是采用简单的对所有输入词求和并求取平均的方法
>           2、隐层到输出层：
>               word2vec采用了霍夫曼树代替隐层到输出层的映射
>               没有了隐层和输出层的softmax概率计算
>
>
>

### word2vec的Hierarchical Softmax：
- **网络结构：**
>       先构造一个权重矩阵W1，然后通过对单词进行hash找到W1(大小为[v,n])所对应的某一行的向量，此向量即为word embedding的向量，
>           然后通过隐层的向量与权重W2(大小为[n,v])进行计算，得到输出向量O,通过对向量O做一个softmax多分类，即可算法每个词出现的概率
>
>       更新权重：
> ![avatar](https://github.com/nwaiting/wolf-ai/blob/master/wolf_others/pic/word2vec_weights_update.png)
>
>       哈夫曼树：
>           各个词在语料中出现的词频当权重构造哈夫曼树
>
>
>

- **CBOW的Hierarchical Softmax：**
>       CBOW：
>           1、通过对周围的词的向量进行加权求取平均值向量，这个平均值向量即为隐层向量的输出，然后和权重矩阵W2进行计算，最后的进行softmax进行多分类
>               训练CBOW时，由于输入是上下文的词向量，需要对输入词向量求平均得到隐层输出向量，然后进行W2的计算
>           2、训练Skip-Gram向量时，选定窗口大小window，对每个词生成2*window个训练样本，注意batch_size的大小必须是2*window的整数倍，确保每个batch包含一个词汇对应的所有样本
>           3、对小型数据集比较适合
>
> ![avatar](https://github.com/nwaiting/wolf-ai/blob/master/wolf_others/pic/word2vec_cbow.png)
>
>       **算法过程：**
>           定义词向量的维度M和CBOW的上下文大小2c，对于训练样本中的每一个词，前面的c个词和后面的c个词作为CBOW的输入，该词作为样本的输出，期望softmax概率最大
>           梯度上升法来更新θ和Xw，这里的Xw是由2c个向量加和平均的结果，而做梯度更新完毕后会用梯度项直接更新原始的各个Xi(i=1,2,...,2c)
>           1、CBOW模型先将词汇表建立成一颗霍夫曼树
>           2、随机初始化所有的模型参数θ和所有的词向量w
>           3、使用梯度上升迭代过程，对于训练集中的每一个样本做梯度计算
>               3.1 计算平均向量Xw
>               3.2 for j = 2 to lw （霍夫曼树内部节点）
>                       g = (1-d-f)η
>                       θ(j-1) = θ(j-1) + gXw
>               3.3 对于context(w)中的每一个词向量xi(共2c个)进行更新
>                       xi= xi + e
>               3.4 如果梯度收敛，则结束梯度迭代，否则回到第3步继续迭代
>
>       **模型输入和输出：！！！！**
>           输入：
>               基于CBOW的预料样本，词向量维度M，CBOW的上下文大小2c，步长η
>           输出：
>               霍夫曼树的内部节点模型参数θ，所有词向量w
>

- **Skip-Gram的Hierarchical Softmax：**
>       Skip-Gram：
>           1、由于输入是一个词向量，所以不需要进行平均
>           2、训练Skip-Gram向量时，选定窗口大小window，对每个词生成2*window个训练样本，注意batch_size的大小必须是2*window的整数倍，确保每个batch包含一个词汇对应的所有样本
>           3、对大语料比较适合
>
>       **与CBOW训练的区别：**
>           CBOW模型对输入进行迭代更新，而Skip-Gram是对2c个输出进行迭代更新
>
>       **参数更新：**
>           通过梯度上升法来更新θ和Xw，如果我们期望P(xi|xw),i=1,2...2c最大，注意上下文是相互的，在期望P(xi|xw)最大的同时，反过来也期望P(xw|xi)最大。
>           那么是使用P(xi|xw)还是P(xw|xi)好，word2vec使用了P(xw|xi)，这样做的好处就是在一个迭代窗口内，我们不是只更新Xw一个词，而是xi,i=1,2...2c共2c个词
>           这样整体的迭代会更加的均衡。
>           由于这个原因，Skip-Gram模型并没有和CBOW模型一样对输入进行迭代更新，而是对2c个输出进行迭代更新。
>
>
>       **算法过程：**
>           1、基于语料训练样本建立霍夫曼树
>           2、随机初始化所有参数θ，所有词向量W
>           3、进行梯度上升迭代，对于训练集的每一个样本(w,context(w))
>               a、for i=1 to 2c:
>                   e = 0
>                   for j = 2 to lw， 计算
>                       g = (1 − d − f)η
>                       θ(j-1) = θ(j-1) + gxi
>               b、如果迭代收敛，则结束，否则回到a步
>
>       **模型输入输出：**
>           输入只有一个词w，输出的是2c个词向量context(w)，期望context(w)这些词的softmax概率比其他词大
>           输入：
>               基于Skip-Gram的训练样本，词向量维度M，Skip-Gram的上下文大小2c，步长η
>           输出：
>               霍夫曼树的内部节点模型参数θ，所有词向量W
>
>

- **对时间复杂度的优化思路：**
>       word2vec对传统的三层神经网络做的改进：
>           1、输入层到隐层的隐射
>               输入层到隐层，**没有采用神经网络的线性变换加激活函数的方法**，而是采用简单的对所有输入词向量求和取平均的方法（求平均值向量）
>           2、隐层到输出的softmax层的计算改进
>               为了避免计算所有词的softmax概率，word2vec采用霍夫曼树代替隐层到输出softmax层的隐射，
>               把之前所有都要计算的概率变成了一颗二叉霍夫曼树，softmax的概率计算只需要沿着树形结构进行就可以了。
>               和传统的神经网络相比：
>                   霍夫曼树的内部节点就类似神经网络隐层的神经元，其中，跟节点的词向量对应我们投影后的词向量，叶子节点对应词汇表大小的输出。！！！
>               由于霍夫曼树是一步步完成计算，所以取名叫"Hierarchical Softmax"。
>               霍夫曼树中的左右子树分类采用二元逻辑回归sigmoid函数完成，沿左子树为负类编码为1，沿右子树为正类编码为0
>
>
>

### word2vec的Negative Sampling：
- **目的：**
>       使用Negative Sampling方法的好处：
>           1、当一个生僻词出现时，会在霍夫曼树中进行深度的计算
>           2、构造霍夫曼树相对Negative Sampling复杂，Negative Sampling计算简单
>
>       思想：
>           对于中心词w和上下文2c个词，记为context(w)，通过负采样得到neg个和w不同的中心词wi,i=1,2,...neg
>           这样context(w)和wi就组成了neg个不真实的负例，然后进行二元逻辑回归，得到负采样对应每个词wi对应的模型参数θi和每个词的词向量
>

- **模型梯度计算：**
>       在逻辑回归中，
>       正例期望：P(context(w0),w0)=σ(Xw0*θw0)
>       负例期望：P(context(w0),wi)=1-P(context(w0),w0)
>       最后我们期望最大化 P(context(w0),w0)∏(P(context(w0),wi))
>       然后得到模型的似然函数以及对应的对数似然函数，和Hierarchical Softmax类似，采用随机梯度上升法，每次只用一个样本更新梯度，迭代更新得到xwi,θwi,i=0,1,...neg
>           这里我们需要求出xw0,θwi,i=0,1,...neg的梯度。
>

- **Negative Sampling负采样方法：**
>       采用的方法有很多，比如大名鼎鼎的MCMC，当时word2vec中的负采样方法比较简单
>       采样前，将长度为1的线段划分成M等分，M>>V，这样可以保证每个词对饮的线段都会划分成对应的小块。而M分中的每一份都会落在某一个词对应的线段上。
>           在采用的时候，只需要从M个位置中采样出neg个位置就行，此时采样到的每一个位置对应到的线段所属的词就是我们的负例词。
>       在word2vec中，M取值默认为10^8
>

- **CBOW的Negative Sampling**
>       模型输入输出
>           输入：
>               基于CBOW训练语料，词向量维度M，上下文2c，步长η，负采样的个数neg
>           输出：
>               词汇表每个词对应的模型参数θ，所有词向量W
>
>       算法训练过程：
>           1、随机初始化所有的模型参数θ和所有的词向量W
>           2、对于每个训练样本(context(w0),w0)，负采样出neg个中心词wi，i=1,2,...neg
>           3、梯度上升迭代过程，对于训练集中的每一个样本(context(w0),wi),i=0,1...neg做如下处理
>               a、e=0, 计算xw0平均向量
>               b、for i= 0 to neg, 计算
>                   e = e + g*θwi
>                   θwi=θwi+g*xw0
>               c、对context(w)中的每一个词向量xk(共2c个)进行更新
>                   xk = xk + e
>               d、如果收敛，结束迭代，否则回到步骤3继续
>

- **Skip-Gram的Negative Sampling：**
>       模型输入输出
>           输入：
>               基于Skip-Gram的训练语料，词向量维度M，上下文大小2c，步长η，采样个数neg
>           输出：
>               词汇表每个词对应的模型参数θ，所有词向量xw
>
>       算法训练过程：
>           1、随机初始化所有模型参数θ，所有词向量W
>           2、对于每个训练样本(context(w0),w0)，负采样出neg个负例中心词wi,i=1,2,...neg
>           3、进行梯度上升迭代过程，对于训练集中的每一个样本(context(w0),wi),i=0,1,...neg
>               a、for i =1 to 2c:
>                   e = 0
>                   for j= 0 to neg, 计算：
>                       e = e + gθwj
>                       θwj=θwj+g*xw0i
>                   词向量更新：
>                       xwoi = xw0i + e
>               b、如果梯度收敛，则结束迭代，否则回到步骤a继续迭代
>
>


- **word2vec的优化点：**
>       1、subsamping
>           对每个词按照一定的概率进行保留或者丢弃
>
>       2、Negative Sampling
>           负采样，没有采用霍夫曼树，每次只是通过采样neg个不同的中心词做负例，就可以训练模型了。
>
>       3、Hierarchical Softmax
>           采用霍夫曼树代替传统的训练方法，可以提高模型训练效率。
>           如果样本中有一个生僻词，那么在霍夫曼树中就要进行深度的搜索，效率不高。这种情况下，使用负采样效率较高。
>           将V分类问题优化成了log(V)次二分类问题，Hierarchical Softmax只是softmax的一种近似形式
>           详解：
>               最先优化和使用的数据结构是用霍夫曼树来代替隐层和输出层的神经元。霍夫曼树的叶子结点起到输出神经元的作用，叶子结点即词汇表的大小。
>               而内部节点则起到隐层神经元的作用。
>           两个优点：
>               1、高频词靠近树根，这样高频词需要更少的时间被找到，符合贪心优化思想
>               2、由于是二叉树，所有计算时间复杂度从O(V)变成了O(log(V))
>
>           逻辑回归（sigmoid）二分类：
>               进行二分类时候需要两个参数
>                   1、当前节点的词向量Xw
>                   2、当前节点的模型参数θ
>               要想得到逻辑回归二分类的参数θ和词向量Xw，使用梯度上升法即可。
>
>           目标：
>               对于Hierarchical Softmax，目标是找到合适的所有节点的词向量和所有内部节点θ，是训练样本达到最大似然。
>
>           如何达到最大似然？
>               使用最大似然法来寻找所有节点的词向量和所有内部节点θ。
>               对于所有样本，我们期望最大化所有样本的似然函数乘积。
>               梯度优化：
>                   在word2vec中，由于使用的是随机梯度上升法，所以并没有把所有样本的似然乘起来得到真正的训练集最大似然，每次
>                   仅仅只用一个样本更新梯度，目的是为了减少梯度计算量。
>               要想得到逻辑回归二分类的参数θ和词向量Xw，使用梯度上升法即可。
>

- **损失函数和优化：**
>       目标函数：
>           思路就是构造一个词及其上下文的条件概率，所有当前词和上下文的条件概率乘积最大化是优化的目标函数
>       优化算法：
>           梯度上升优化算法，最大化最大似然函数，得到模型参数和词向量
>
>
>
>
>
>
>

- **霍夫曼编码：**
>       霍夫曼树的构造：
>           1、看做是n颗树的森林，每一棵树仅有一个节点
>           2、对所有的树进行合并
>
>       约定编码：
>           可以约定如左子树编码为1，右子树编码为0，则可以对任一叶子节点进行01编码
>
>
>
>

- **待续：**
>       参考：https://www.cnblogs.com/pinard/p/7243513.html
>           https://www.zybuluo.com/evilking/note/871910
>           http://shomy.top/2017/07/28/word2vec-all/
>
>
>
>
>
>
>
>
>
>
>
>
>
