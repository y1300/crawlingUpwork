## Codes

### Getting User IDs
# getId.py
To get IDs of freelancers used in the website. Should run several times to crawl as much ids as possible, due to limited number (500) of pages we can access at all times, the dynamical ordering of this IDs. Hidden IDs located in pages inaccessible can show up sometimes. These intermedia results are written in "Output.txt".

# getId_tor.py
To get IDs with dynamic ip addresses via Tor network. Increasing the chance of being blocked. These intermedia results are written in "Output.txt".

# getUniqueId.py
To get IDs with no repetition from "Output.txt". Unique IDs are in "ids.txt"



## Output

# items.jl
items.jl is just a plain text file with each freelancer's profile on one line, the structure of each item is "key": "value" with commas separating itmes from each other.

The items including:
- webpage: the webpage of this profile
- id: the id of this freelancer
- title: the title of this profile
- name: freelancers' name
- shortName: freelancers' name in short
- description: the introduction of freelancer
- location: where they live
- portrait: the url of the photo on profile
- skills: the skill of the freelancer
- totalHours: hours working on Upwork.com in total
- totalFeedback: feedbacks them gained in total
- totalJobsWorked: jobs they took in history
- rating: overall rating
- hourlyRate: the prefered amount paid by hour
- totalPortfolioItems: total number of portfolios shown on the porfile
- englishLevel: freelancers' English level
- memberSince: the date joined the Upwork.com
- lastWorkedOn: the date of last job
- hireAgainPercentage: the percentage of their jobs being hired by the same employer again
- totalHourlyJobs: all the jobs being paid by hour
- totalFixedJobs: all the jobs being paid by fixed amount
- totalRevenue: total profit gained in history
- skillTestsPassed: number of skill tests passed
- portfolios: the descriptions of their portfolios
- portfoliosImage: the images of portfolios
- education: the education of freelancers
- assignments_startedOn: the starting date of this job
- assignments_endedOn: the ending date of this job
- assignments_totalCharges: the earning of this job
- assignments_totalHours: total lasting time of this job
- assignments_hourlyRate: the amount paid by hour of this job
- assignments_title: the title of this job
- assignments_feedback_score: the rating of this job
- assignments_feedback_comment: the comment of this job

# rankedBySentiments.txt
gives the id, name and corresponding sentiment score of one freelancer, based on sentiment analysis on the descriptions of freelancers about themselves. The sentiment score is a float between [-1.0,1.0], and larger numbers mean more positive sentiments and thus resulting in higher ranking.

The structure of the list is: each line represent one freelancer, consisting by the "sentiment score", "id", "name" and "description" in order, which separated by commas. The "id" can be used as following to access each profile.

    $ https://www.upwork.com/o/profiles/users/~id
    
# Image
The image.tar.gz contains all the portraits of the freelancers based in China (around 92% of them has uploaded photos), and the folder image/full contains a few examples of these photos.

## Clone

    $ git clone git://github.com/y1300/crawlingUpwork.git
