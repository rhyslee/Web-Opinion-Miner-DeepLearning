### Unit Test module for web scraper,
### function:
### try to fetch a list of articles
### checkingPoints:
### 1.Able to sucessfully fetch content from the designated web URL
### 2.Correct parsing of article title, author, source, date, text
### 3.Able to correectly filter out result unqualified with filter rules.

from .. import articles_filter
from .. import web_scraper

test_filter  =
test_scraper = web_scraper.WebScraper
test_URL = 'http://...'
test_topics = ["tax","tax reform"]
test_keywords = ["tax","reform", "taxation"]
test_timeFilter = ["01/01/2015"]
test_scraper.searchByURL(test_topics,test_timeFilter,test_keywords)