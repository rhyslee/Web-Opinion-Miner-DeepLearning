import json
from pprint import pprint
from newspaper import Article

with open('156_obamacare_nytimes_articles_urls.json') as data_file:    
    data = json.load(data_file)

parsed_dataset = []

for i in data:
	url = i["url"]
	title = i["title"]
	article = Article(url)
	article.download()
	article.parse()
	parsed_article = article.text
	parsed_article = parsed_article.replace("\n\n", " ")

	article_item = {"title" : title, "url" : url, "parsed_article" : parsed_article}
	parsed_dataset.append(article_item)

with open('extracted_nytimes_articles.json', 'w') as outfile:  
    json.dump(parsed_dataset, outfile, indent=4)
