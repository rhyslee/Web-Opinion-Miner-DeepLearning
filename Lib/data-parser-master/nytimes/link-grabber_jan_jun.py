import re
import requests
import json


begin_date = "" #yyyymmdd
end_date = "" #yyyymmdd
sort = ""

parsed_dataset = []

#data parsing function
def dataparser(end_date, begin_date, sort, page_number):
	page = str(page_number)
	print("extracting data for %s - %s" % (begin_date, end_date))

	url = "http://query.nytimes.com/svc/add/v1/sitesearch.json?end_date=" + end_date + "&begin_date=" + begin_date + "&sort=" + sort + "&page=" + page + "&fq=document_type%3A%22article%22%20AND%20section_name:%22Opinion%22%20OR%20subsection_name:%22Opinion%22&facet=true"

	response = requests.get(url)

	if response.status_code == 200:
		response = response.json()
		response = response["response"]["docs"]

		if response == []:
			return

		# response = response.json()

		for i in response:
			i_url = i["web_url"]
			i_head = i["headline"]["main"]
			i_pub_date = i["pub_date"]

			k = {"tile" : i_head, "url" : i_url, "date" : i_pub_date}

			parsed_dataset.append(k)

		print("Data extracted for page %s" % page)
		return

	else:
		print("response error")
		return

	return

sort = "asc"


begin_date = "20160101" #yyyymmdd
end_date = "20160131" #yyyymmdd
print("saving urls for january")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160201" #yyyymmdd
end_date = "20160228" #yyyymmdd
print("saving urls for february")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160301" #yyyymmdd
end_date = "20160331" #yyyymmdd
print("saving urls for march")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160401" #yyyymmdd
end_date = "20160430" #yyyymmdd
print("saving urls for april")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160501" #yyyymmdd
end_date = "20160531" #yyyymmdd
print("saving urls for may")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160601" #yyyymmdd
end_date = "20160630" #yyyymmdd
print("saving urls for june")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

with open('nytimes_articles_urls.json', 'w') as outfile:  
    json.dump(parsed_dataset, outfile, indent=4)




# for i in response:
# 	response = response["response"]["docs"][i]
# 	print(response)


# print(response)

# response_urls = re.match(r'https:\/\/www.nytimes.com\/\d+\/\d+\/\d+\/opinion\/', response)

# print(response_urls)
# print(response.json())

# links = linkGrabber.Links(response.text)

# links = links.find()
# print(links)

# links = linkGrabber.Links("http://query.nytimes.com/search/sitesearch/#/*/from20160101to20161231/allresults/1/allauthors/newest/Opinion/")

# links = links.find()

# print(links)

# url = "http://query.nytimes.com/search/sitesearch/#/*/from20160101to20161231/allresults/1/allauthors/newest/Opinion/"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# response = requests.get(url, headers=headers)

# print(response.content)