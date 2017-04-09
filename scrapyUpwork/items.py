# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyupworkItem(scrapy.Item):
    # define the fields for your item here like:
    webpage = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    shortName = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    portrait = scrapy.Field()
    # bigPortrait = scrapy.Field()
    # bigPortrait = scrapy.Field()
    # originalPortrait = scrapy.Field()
    skills = scrapy.Field()
    totalHours = scrapy.Field()
    totalFeedback = scrapy.Field()
    totalJobsWorked = scrapy.Field()
    rating = scrapy.Field()
    hourlyRate = scrapy.Field()
    totalPortfolioItems = scrapy.Field()
    englishLevel = scrapy.Field()
    memberSince = scrapy.Field()
    lastWorkedOn = scrapy.Field()
    hireAgainPercentage = scrapy.Field()
    totalHourlyJobs = scrapy.Field()
    totalFixedJobs = scrapy.Field()
    totalRevenue = scrapy.Field()
    skillTestsPassed = scrapy.Field()
    portfolios = scrapy.Field()
    portfoliosImage = scrapy.Field()
    memberSince = scrapy.Field()
    education = scrapy.Field()

    assignments_startedOn = scrapy.Field()
    assignments_endedOn = scrapy.Field()
    assignments_totalCharges = scrapy.Field()
    assignments_totalHours = scrapy.Field()
    assignments_hourlyRate = scrapy.Field()
    # assignments_type = scrapy.Field()
    assignments_title = scrapy.Field()
    assignments_feedback_score = scrapy.Field()
    assignments_feedback_comment = scrapy.Field()


    hourlyRate = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()

    pass
