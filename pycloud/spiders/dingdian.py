import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from pycloud.items import DingdianItem

class MySpide(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['23us.so']
    bash_rul = 'http://www.23us.so/list/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1,10):
            url = self.bash_rul + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23us.so/full.html', self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_= 'pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            a_tag = td.find('a')
            novelname = a_tag.get_text()
            novelurl = a_tag['href']
            yield Request(novelurl, callback=self.get_chapterurl, meta={'name':novelname, 'url': novelurl})

    def get_chapterurl(self, response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url).split('/')[-2]
        item['category'] = str(category).replace('\xa0', '')
        item['author'] = str(author).replace('\xa0', '')
        item['name_id'] = name_id
        yield item
        yield Request(url=bash_url, callback=self.get_chapter, meta={'name_id':name_id})

    def get_chapter(self):
        urls = re.findall('')
