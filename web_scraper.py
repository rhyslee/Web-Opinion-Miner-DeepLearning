### web_scrapper.py
### loaded by feed_preprocessor.py
import debug_helper
import articles_filter
import Lib.Article_Extractor
import Lib.Parser

# load
debugger = debug_helper.debug_config()
debug_helper.greetings()


class AdapterExtractor:
    def __init__(self, _extractor):
        self.extractor = _extractor

    def fetch_by_url(self, _url):
        # download text contents from the URL
        fetched_text = ""
        return fetched_text


class AdapterParser:
    def __init__(self, _parser):
        self.parser = _parser

    def parse_text(self, _text):
        parsed_text = ['']
        return parsed_text


class WebScraper:

    def __init__(self, _article_filter):
        self.filter = _article_filter

        # interface the given code from extractor and parser.
        self.extractor = AdapterExtractor
        self.parser = AdapterParser

    def search_by_url(self, _url):
        web_text = self.extractor.fetch_by_url(_url)
        parsed_text = self.parser.parse_text(web_text)




