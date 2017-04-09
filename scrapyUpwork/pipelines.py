# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ScrapyupworkPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'ab')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

# class MyImagePipelines(ImagesPipeline):
#   def file_path(self, request, response=None, info=None):
#       image_guid = request.url.split('/')[-1]
#       return 'full/%s' % (image_guid)

#   def get_media_requests(self, item, info):
#       for image_url in item['image_urls']:
#           yield Request(image_url)

#   def item_completed(self, results, item, info):
#       image_paths = [x['path'] for ok, x in results if ok]
#       if not image_paths:
#           raise DropItem("Item contains no images")
#       return item

class MyImagePipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url, meta={'item': item})
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0[name]}/{0[id]}/{1}'.format(item, image_guid)
        return filename
