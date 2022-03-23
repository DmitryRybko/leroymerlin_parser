# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class LeroyparserPipeline:
    def process_item(self, item, spider):
        return item


class LeroyPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['image_urls']:
            for photo in item['image_urls']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(e)


