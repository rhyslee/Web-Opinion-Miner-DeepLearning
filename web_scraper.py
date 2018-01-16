### web_scrapper.py
### loaded by feed_preprocessor.py
import debug_helper
import articles_filter
import Lib.Article_Extractor
import Lib.Parser


#load
debugger = debug_helper.debug_config()
debug_helper.greetings()

class scraper:
    def __init__(self):
        self.extrator # interface the given code from extractor and parser.
        self.parser
