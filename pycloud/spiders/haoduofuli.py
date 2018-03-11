from scrapy.spiders import CrawlSpider, Request, Rule
from scrapy.linkextractors import LinkExtractor
from pycloud.items import HaoduofuliItem
from scrapy import FormRequest
import logging

class MySpider(CrawlSpider):
    name = 'haoduofuli'
    allowed_domains = ['39.106.63.121']
    start_urls = ['http://39.106.63.121/index.php']
    rules = (
        Rule(LinkExtractor(allow=('\.php',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.text)
        pass