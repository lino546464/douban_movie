# -*- coding: utf-8 -*-
from scrapy import Selector,Spider,Request
from lxml import etree
from ..items import   DoubanmovieItem

class TopmoviesSpider(Spider):
    name = 'topmovies'
    # allowed_domains = ['www.douban.com']
    # start_urls = ['https://movie.douban.com/top250']
    base_url = 'https://movie.douban.com/top250'
    def start_requests(self):
        yield Request(self.base_url,self.get_movie)
    def get_movie(self, response):
        item = DoubanmovieItem()
        select = Selector(response)
        its = select.xpath('//ol[@class="grid_view"]/li/div/div[@class="info"]')
        for it in its:
            title = str(it.xpath('div[@class="hd"]/a/span[1]/text()').extract()[0]).strip()
            url = str(it.xpath('div[@class="hd"]/a/@href').extract()[0]).strip()
            text = str(it.xpath('div[@class="bd"]/p[1]/text()').extract()[0]).strip()
            star = str(it.xpath('div[@class="bd"]/div/span[2]/text()').extract()[0]).strip()
            content = str(it.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]).strip()
            item['title'] = title
            item['url'] = url
            item['text'] = text
            item['star'] = star
            item['content'] = content
            print(title,url,text,star,content)
            yield item

        next_page = select.xpath('//div[@class="paginator"]/span[@class="next"]')
        if next_page:
            n_url = next_page.xpath('link/@href').extract()[0]
            next_url = self.base_url + n_url
            print(next_url)
            yield Request(next_url,self.get_movie)