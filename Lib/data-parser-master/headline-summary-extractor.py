import json
import requests
import newspaper

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

#News API
sources_url = 'https://newsapi.org/v1/sources?language=en&country=us&category=general'
newsapi_key = 'e7a281c9e8de431f941833b35323e448'

#Extracts ids of popular news sources in the US available from newsapi
sources = requests.get(sources_url)
sources = sources.json()
sources = sources["sources"]

source_ids = []
for i in sources:
	for key, value in i.items():
		if key == "id":
			source_ids.append(value)
print(source_ids)

#Generate api urls for news extraction
source_urls = []

for i in source_ids:
	url = "https://newsapi.org/v1/articles?source=%s&apiKey=%s" % (i, newsapi_key)
	source_urls.append(url)

print(source_urls)

#extract headlines and summary from top articles

for i in source_urls:
	articles = requests.get(i)
	articles = articles.json()

	print(articles)





