import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['baocai.com']
    start_urls = [
        "https://www.baocai.com/invest/general/index.html",
        "http://www.baocai.com/help/index.html"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)