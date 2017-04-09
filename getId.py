# Crawling user Ids without Tor network and dynamic IP addresses

import urllib2
import stem
import stem.connection
from stem import Signal
from stem.control import Controller
import re
import time
import random
from fake_useragent import UserAgent

# The fake user agent
ua = UserAgent()

# The url where we looking for user Ids
url = 'https://www.upwork.com/o/profiles/browse/?loc=china&page='
# Pages allow to access
pages = range(1,501)
# Random permutation of accessing
random.shuffle(pages)


class Upwork:

	def __init__(self):
		self.pageIndex = 0 # To show how many pages we've crawled
		self.user_agent = ua.random
		self.url = url + str(pages[self.pageIndex])
		self.referer = url + str(pages[self.pageIndex])
		self.headers = {
			'User-Agent' : self.user_agent,
			'Referer' : self.referer, 
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, image/webp, */*;q=0.8',
			'Accept-Language': "en-GB,en;q=0.8,zh-CN;q=0.6",
			'Accept-Encoding' : 'gzip, deflate, sdch',
			'Connection' : 'close'
		}

	# To get the whole page
	def getPage(self):
		try:
			self.url = url + str(pages[self.pageIndex])
			print self.url
			request = urllib2.Request(url = self.url, data = None, headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read()
			return pageCode

		# Show error when fail to request a page
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print "getPage: ERROR:", e.code, e.reason
				return None

	# To get user ids from the page
	def getId(self, pageCode):
		pattern = re.compile('data-log-data=.*?"id":"(~.*?)"')
		items = re.findall(pattern,pageCode)
		return items
			
	# To start the procedure
	def start(self):
		pageCode = self.getPage()
		# print self.user_agent
		if pageCode != None:
			id = self.getId(pageCode)
			print id

			# Raw output, append method used
			text_file = open("Output.txt", "a")
			text_file.write('\n'.join(id))
			text_file.write('\n')
			text_file.close()
			self.pageIndex += 1
			return 1
		else:
			return 0


if __name__ == "__main__":

	crawlable = 0
	spider = Upwork()

	while spider.pageIndex < 500:

		while not crawlable:
			crawlable = spider.start()

		print ("PageIndex: %d" % (spider.pageIndex))
		time.sleep( 15 + random.uniform(-1,1) ) # sleep for 15 seconds between each page is safer