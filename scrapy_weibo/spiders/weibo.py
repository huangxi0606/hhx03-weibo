# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['https://weibo.com']
    start_urls = ['http://https://weibo.com/']

    def parse(self, response):
        pass
