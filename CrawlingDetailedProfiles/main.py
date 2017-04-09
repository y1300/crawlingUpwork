from scrapy import cmdline

# To get the login page as an example
# cmdline.execute("scrapy crawl login".split())

# To get one profile page with login as an example
# cmdline.execute("scrapy crawl testIndependent".split())

# To get profiles without login
# cmdline.execute("scrapy crawl withoutLoginIndependent".split())

# To get profile with login
cmdline.execute("scrapy crawl Independent".split())