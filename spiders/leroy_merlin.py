import scrapy
from scrapy.http import HtmlResponse
from items import LeroyparserItem
from scrapy.loader import ItemLoader


class LeroySpider(scrapy.Spider):
    name = 'leroy_merlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://leroymerlin.ru/search/?q={kwargs.get('search')}&eligibilityByStores=ЗИЛ"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//div[contains(@class, 'largeCard')]//a")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name', "//h1[@slot='title']/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_value('url', response.url)
        loader.add_xpath('image_urls', "//picture[@slot='pictures']/source[@media='only screen and (min-width: "
                         "768px)']/@srcset")
        yield loader.load_item()
