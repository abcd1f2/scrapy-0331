# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WebspiderPipeline(object):
    def __init__(self,v=None):
        self.value = v

    def process_item(self, item, spider):
        #to do 存储等
        print 'WebspiderPipeline process'
        return item

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        #val = crawler.settings.getint('MMMM')
        #return cls(val)
        return cls()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('WebspiderPipeline open')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('WebspiderPipeline close')

class WebspiderPipelineIqiyi(object):
    def __init__(self):
        self.file_name = 'iqiyi.data'
        self.savefile = None
        pass

    def process_item(self, item, spider):
        #to do 存储等
        #print 'WebspiderPipelineIqiyi process'
        #from webspider.items import WebspiderPipelineIqiyiItem
        #item = WebspiderPipelineIqiyiItem()
        #s = "{0}, {1}, {2}, {3}".format(item['name'], item['score'], item['actors'], item['isvip'])
        #self.savefile.write(s)
        #print u"{0} {1}".format(item['name'], item)
        #self.savefile.write(json.dumps(dict(item), encoding='utf-8') + "\n")
        self.savefile.write(u"{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}\n".format(item['name'], item['score'], item['isvip'],
         item['totalcomments'], item['playcounts'], item['upcounts'], item['downcounts'], item['actors']))
        #raise DropItem()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipelineIqiyi open')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipelineIqiyi close')

class WebspiderPipelinePPTV(object):
    def __init__(self):
        self.file_name = 'pptv.data'
        self.savefile = None
        pass

    def process_item(self, item, spider):
        #to do 存储等
        #print 'WebspiderPipelinePPTVItem process'
        self.savefile.write(u"{0}-{1}-{2}-{3}-{4}\n".format(item['name'], item['score'], item['isvip'], item['fileurl'], item['details']))
        #raise DropItem()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipelinePPTVItem open')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipelinePPTVItem close')

class WebspiderPipelineTieBa(object):
    def __init__(self):
        self.file_name = 'baidu.tieba.data'
        self.savefile = None

    def process_item(self, item, spider):
        """
            title = scrapy.Field()
            author = scrapy.Field()
            authorlevel = scrapy.Field()
            responsenum = scrapy.Field()
            frescontent = scrapy.Field()
            fresuser = scrapy.Field()
            frestime = scrapy.Field()
        """
        self.savefile.write(u"{0}-{1}-{2}-{3}-{4}-{5}-{6}\n".format(item['title'], item['author'], item['authorlevel'], item['responsenum'], item['frescontent'], item['fresuser'], item['frestime']))
        #raise DropItem()

    def open_spider(self,spider):
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipelineTieBaItem open')

    def close_spider(self,spider):
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipelineTieBaItem close')

class WebspiderPipeline36kr(object):
    def __init__(self):
        self.file_name = '36kr.company.data'
        self.savefile = None

    def process_item(self, item, spider):
        """
        name = scrapy.Field()
        brief = scrapy.Field()
        #行业
        industry = scrapy.Field()
        # 第几轮
        pphase = scrapy.Field()
        #所在地
        city = scrapy.Field()
        #成立时间
        time = scrapy.Field()
        """
        self.savefile.write(u"{0}-{1}-{2}-{3}-{4}-{5}\n".format(item['name'], item['industry'], item['phase'], item['city'], item['time'], item['brief']))
        #raise DropItem()

    def open_spider(self,spider):
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipeline36krItem open')

    def close_spider(self,spider):
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipeline36krItem close')


class WebspiderPipelineAizhan(object):
    def __init__(self):
        self.file_name = 'aizhan.allwords.data'
        self.savefile = None

    def process_item(self, item, spider):
        """
        """
        self.savefile.write(u"{0}\n".format(item['word']))
        #raise DropItem()

    def open_spider(self,spider):
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipelineAizhan open')

    def close_spider(self,spider):
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipelineAizhan close')

class WebspiderPipelineJD(object):
    def __init__(self):
        self.file_name = 'jd.allwords.data'
        self.savefile = None

    def process_item(self, item, spider):
        """
            comments = scrapy.Field()
            referenceName = scrapy.Field()
            referenceTime = scrapy.Field()
            productColor = scrapy.Field()
            productSize = scrapy.Field()
        """
        tmp_dict = {}
        tmp_dict['comments'] = item['comments']
        tmp_dict['referenceName'] = item['referenceName']
        tmp_dict['referenceTime'] = item['referenceTime']
        tmp_dict['productColor'] = item['productColor']
        tmp_dict['productSize'] = item['productSize']
        self.savefile.write(u"{0}\n".format(json.dumps(tmp_dict)))
        #raise DropItem()

    def open_spider(self,spider):
        try:
            self.savefile = open(self.file_name, 'w')
        except Exception as e:
            print "open file {0} error {1}".format(self.file_name, e)

        print('WebspiderPipelineJD open')

    def close_spider(self,spider):
        try:
            self.savefile.close()
        except Exception as e:
            print "close file {0} error {1}".format(self.file_name, e)
        print('WebspiderPipelineJD close')
