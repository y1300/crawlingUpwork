from scrapy.selector import Selector
from scrapy.http import Request
import scrapy
class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["www.upwork.com"]

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.upwork.com/"
    }

    cookies = {open('cookie.txt','r').read()}

    def start_requests(self):
        return [Request("https://www.upwork.com/freelancers/~0179a2443f008072b1",cookies = self.cookies,headers=self.headers)]

    def parse(self, response):
        item = Selector(response)
        with open("login.html",'w') as pf:
            pf.write(item.extract().encode('utf-8'))