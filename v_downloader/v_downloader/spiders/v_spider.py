import scrapy
import time

class VSpider(scrapy.Spider):
    name = "videoSpider"

    def start_requests(self):
        self.urls = []
        with open("../../url_addr_parsed.txt", "r") as f:
            self.urls = f.readlines()
        
        for url in self.urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse_first)

    def parse_first(self, response):
        pass