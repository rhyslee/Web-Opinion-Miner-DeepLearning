#   articles_filter.py
#   loaded by web_scrapper.py

import time
from datetime import date, datetime

# default cut off time is today so that
#  this is yb default not going to clog the algo
today = date.today();
sample_date_string = "31/12/2015"


def getDateFromString(_dateString):
    newDate = datetime.strptime(_dateString, "%d/%m/%Y")
    return newDate


# _earliestAcecptTime is a list of date in this format:
# sample_date_string = "31/12/2015"
class ArticleFilter:
    timeFilter = today
    topics = []
    keywords = []

    def __init__(self, _topics, _earliest_accepted_time, _keywords):
        for i, item in enumerate(_topics):
            self._topics.append(_topics)
            print(self.topics[i])

        for i, item in enumerate(_earliest_accepted_time):
            self.timeFilters.append(getDateFromString(item))
            print(self.timeFilters[i])

        for i, item in enumerate(_keywords):
            self.keywords.append(_keywords)
            print(self.keywords[i])

