import re
import requests
import json


page=""
parsed_dataset = []
query = ""


def parser(query, page):
	page = str(page)
	url = ("http://query.nytimes.com/svc/add/v1/sitesearch.json?q=" + query + "&end_date=20161231&begin_date=20160101&sort=desc&page=" + page + "&fq=document_type%3A%22article%22%20AND%20section_name:%22Opinion%22%20OR%20subsection_name:%22Opinion%22&facet=true")

	response = requests.get(url)

	if response.status_code == 200:
		response = response.json()
		results = response["response"]["docs"]

		if (results == []):
			return
		else:

			for i in results:
				article_url = i["web_url"]
				article_head = i["headline"]["main"]
				article_pub_date = i["pub_date"]

				link_item = {"title" : article_head, "url" : article_url, "date" : article_pub_date}
				parsed_dataset.append(link_item)

			print("Data extracted for page %s" % page)
			return

query = input('Please enter a topic (one word): ')

for page in range(0,50):
	parser(query, page)

x = 0
for i in parsed_dataset:
	x += 1

x = str(x)
print( x + " articles extracted for " + query)

with open(x + '_' + query + '_nytimes_articles_urls.json', 'w') as outfile:  
    json.dump(parsed_dataset, outfile, indent=4)



