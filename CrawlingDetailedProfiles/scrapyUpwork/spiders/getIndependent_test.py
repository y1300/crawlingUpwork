from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from scrapy.utils.response import get_base_url
from scrapyUpwork.items import *
import scrapy
import logging
import json
import re

class IndepentSpider(scrapy.Spider):
    name = "testIndependent"
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

    # s = '{' + open('cookie.txt','r').read() + '}'
    # cookies = json.loads(s)

    def start_requests(self): 
        return [Request("https://www.upwork.com/ab/account-security/login", meta={'cookiejar': 1}, callback=self.post_login, headers=self.headers)]


    def post_login(self, response):
        login__token = response.xpath(
            '//input[@name="login[_token]"]/@value').extract_first()
        logging.info('login[_token]=' + login__token)
        return [FormRequest.from_response(response,
            url='https://www.upwork.com/ab/account-security/login',
            # cookies = self.cookies,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata={
              'login[username]': 'yc1300',
              'login[password]': '13006215630yc',
              'login[_token]': login__token
            },
            callback=self.after_login,
            dont_filter=True
            )]

    def after_login(self, response):
        return [Request("https://www.upwork.com/freelancers/~01e200ab864accf375/",
            # cookies = self.cookies,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers)]


    def getItem(self,item, response, info):
        # try:

        item['webpage'] = get_base_url(response)

        item['id'] = get_base_url(response)[-20:-1]
        
        pattern = re.compile('profile.*?title.*?:(.*?),')
        item['title'] = re.findall(pattern,info[0])[0].strip('\"') #sel.xpath('//title/text()').extract()[0].encode('ascii').strip(' \n')
        
        pattern = re.compile('profile.*?name.*?:(.*?),')
        item['name'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('profile.*?shortName.*?:(.*?),')
        item['shortName'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('profile.*?description.*?:(.*?)\\",')
        item['description'] = re.findall(pattern,info[0])[0].strip('\"').replace('\\n',' ')

        pattern = re.compile('profile.*?location.*?:(.*?})')
        item['location'] = re.findall(pattern,info[0])[0].replace('\"','').replace('\\','')

        pattern = re.compile('profile.*?portrait.*?portrait":(.*?),')
        item['portrait'] = re.findall(pattern,info[0])[0].strip('\"').replace('\\','')

        pattern = re.compile('"skills":(.*?),"visibility"')
        tempSkills = (',').join(re.findall(pattern,info[0]))
        pattern = re.compile('"prettyName":(".*?"),"active"')
        item['skills'] = '{'+(',').join(re.findall(pattern,tempSkills)).replace('\"','')+'}'

        pattern = re.compile('education.*?("institutionName.*?,).*?("areaOfStudy.*?,).*?("degree.*?,).*?("dateStarted.*?,).*?("dateEnded.*?,)')
        item['education'] = '{'+('').join(str(re.findall(pattern,info[0]))).replace('\"','')+'}'

        pattern = re.compile('hideJss.*?stats.*?totalHours.*?:(.*?),')
        item['totalHours'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalFeedback.*?:(.*?),')
        item['totalFeedback'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalJobsWorked.*?:(.*?),')
        item['totalJobsWorked'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?rating.*?:(.*?),')
        item['rating'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?hourlyRate.*?amount.*?:(.*?)},')
        item['hourlyRate'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalPortfolioItems.*?:(.*?),')
        item['totalPortfolioItems'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?englishLevel.*?:(.*?),')
        item['englishLevel'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?memberSince.*?:(.*?),')
        item['memberSince'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?lastWorkedOn.*?:(.*?),')
        item['lastWorkedOn'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?hireAgainPercentage.*?:(.*?),')
        item['hireAgainPercentage'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalHourlyJobs.*?:(.*?),')
        item['totalHourlyJobs'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalFixedJobs.*?:(.*?),')
        item['totalFixedJobs'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?totalRevenue.*?:(.*?),')
        item['totalRevenue'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('hideJss.*?stats.*?skillTestsPassed.*?:(.*?),')
        item['skillTestsPassed'] = re.findall(pattern,info[0])[0].strip('\"')

        pattern = re.compile('portfolios(.*?)competencies')
        tempstr = re.findall(pattern,info[0])[0]
        pattern = re.compile('title.*?:(.*?),')
        tempstr = ','.join(re.findall(pattern,tempstr))
        item['portfolios'] = '{' + tempstr.replace('\"','') + '}'

        pattern = re.compile('portfolios(.*?)competencies')
        tempstr = re.findall(pattern,info[0])[0]
        pattern = re.compile('image.*?:(.*?),')
        tempstr = ','.join(re.findall(pattern,tempstr))
        item['portfoliosImage'] = '{' + tempstr.replace('\"','').replace('\\','') + '}'

        pattern = re.compile('competencies.*?assignments(.*?)availability')
        assignments = re.findall(pattern,info[0])[0]

        pattern = re.compile('startedOn.*?:(.*?),')
        assignments_startedOn = ','.join(re.findall(pattern,assignments))
        item['assignments_startedOn'] = '{' + assignments_startedOn.replace('\"','') + '}'

        pattern = re.compile('endedOn.*?:(.*?),')
        assignments_endedOn = ','.join(re.findall(pattern,assignments))
        item['assignments_endedOn'] = '{' + assignments_endedOn.replace('\"','') + '}'

        pattern = re.compile('totalCharges.*?amount.*?:(.*?)}')
        assignments_totalCharges = ','.join(re.findall(pattern,assignments))
        item['assignments_totalCharges'] = '{' + assignments_totalCharges.replace('\"','') + '}'

        pattern = re.compile('totalHours.*?:(.*?),')
        assignments_totalHours = ','.join(re.findall(pattern,assignments))
        item['assignments_totalHours'] = '{' + assignments_totalHours.replace('\"','') + '}'

        pattern = re.compile('hourlyRate.*?amount.*?:(.*?)}')
        assignments_hourlyRate = ','.join(re.findall(pattern,assignments))
        item['assignments_hourlyRate'] = '{' + assignments_hourlyRate.replace('\"','') + '}'

        # pattern = re.compile('type.*?:(.*?),') # type 1 is fixed term
        # assignments_type = ','.join(set(re.findall(pattern,assignments)))
        # item['assignments_type'] = '{' + assignments_type.replace('\"','') + '}'

        pattern = re.compile('title.*?:(.*?),')
        assignments_title = ','.join(re.findall(pattern,assignments))
        item['assignments_title'] = '{' + assignments_title.replace('\"','').replace('\\','') + '}'

        pattern = re.compile('feedback.*?score.*?:(.*?),')
        assignments_feedback_score = ','.join(re.findall(pattern,assignments))
        item['assignments_feedback_score'] = '{' + assignments_feedback_score.replace('\"','') + '}'

        pattern = re.compile('feedback.*?comment.*?:(".*?")')
        assignments_feedback_comment = ','.join(re.findall(pattern,assignments))
        item['assignments_feedback_comment'] = '{' + assignments_feedback_comment.replace("\\n",' ').replace('\\','')  + '}'

        # pattern = re.compile('profile.*?portrait.*?portrait":(.*?),')
        item['image_urls'] = [item['portrait']]
        # # except:
        # #     print 'ERROR'

        return item

    def handle_error(self, failure):
        self.log("Request failed: %s" % failure.request)

    def parse(self, response):
        sel = Selector(response)
        info = sel.xpath('//script[@type="text/javascript"]').re("'/freelancers';\n(.*?)\n.*?angularCache")

        item = ScrapyupworkItem()
        item = self.getItem(item, response, info)

        yield item