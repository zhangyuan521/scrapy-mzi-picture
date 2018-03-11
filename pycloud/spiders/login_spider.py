import scrapy

class LoginSpider(scrapy.Spider):
    name = 'duke.com'
    start_urls = ['http://39.106.63.121/index.html']

    def parse(self, response):
        print(response.body)
        return scrapy.FormRequest.from_response(response,formdata={'title':'zhangyuan'},callback=self.after_login)

    def after_login(self, response):
        print(response.body)