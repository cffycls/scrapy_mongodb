import scrapy
 
class TxmoviesItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()


class TxmoviesPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class TxmsSpider(scrapy.Spider):
    name = 'txsp'
    allowed_domains = ['v.qq.com']
    start_urls = ['https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset=0&pagesize=30']
    offset=0
 
    def parse(self, response):
        print('=====================')
        items=TxmoviesItem()
        lists=response.xpath('//div[@class="list_item"]')
        for i in lists:
            items['name']=i.xpath('./a/@title').get()
            items['description']=i.xpath('./div/div/@title').get()
 
            yield items
 
        if self.offset < 120:
            self.offset += 30
            url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'.format(
                str(self.offset))
 
            yield scrapy.Request(url=url,callback=self.parse)
            
        print('=====================')