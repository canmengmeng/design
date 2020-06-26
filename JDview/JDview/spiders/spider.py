import scrapy

from ..items import JdviewItem

import json
import csv, os



class JdViewSpider(scrapy.Spider):
    name = 'JdView'
    allowed_domains = ['jd.com']
    item_id = 100009691096
    pos_file = 'pos.csv'
    neg_file = 'neg.csv'
    now_file = pos_file
    # 3: pos    1: neg
    score = 3
    start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=&productId=' + str(item_id) + '&score=' + str(score) + '&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1']

    def parse(self, response):
        jdCommentJson = json.loads(response.text.lstrip('(').rstrip(')'))
        comments = jdCommentJson['comments']  # 上步将JSON字符串转化为Python字典格式
        maxPage = jdCommentJson['maxPage']
        for comment in comments:
            content = comment['content'].strip().replace('\n', ' ')
            item = JdviewItem(content=content)
            if not os.path.exists(self.now_file):
                csvfile = open(self.now_file, 'a+', newline='', encoding='utf-8')
                write = csv.writer(csvfile)
                write.writerow(['content'])
            else:
                csvfile = open(self.now_file, 'a+', newline='', encoding='utf-8')
                write = csv.writer(csvfile)
            write.writerow([item['content']])
            csvfile.close()
            yield item
        for page in range(1, maxPage):
            next_url = 'https://club.jd.com/comment/productPageComments.action?callback=&productId=' + str(self.item_id) + '&score=' + str(self.score) + '&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&fold=1'
            yield scrapy.Request(next_url, callback=self.parse)