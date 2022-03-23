from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import settings
from spiders.leroy_merlin import LeroySpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    search = 'электрогенераторы'
    process.crawl(LeroySpider, search=search)

    process.start()
