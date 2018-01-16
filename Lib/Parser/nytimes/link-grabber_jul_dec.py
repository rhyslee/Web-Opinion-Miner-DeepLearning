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


begin_date = "20160701" #yyyymmdd
end_date = "20160731" #yyyymmdd
print("saving urls for july")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160801" #yyyymmdd
end_date = "20160831" #yyyymmdd
print("saving urls for august")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20160901" #yyyymmdd
end_date = "20160930" #yyyymmdd
print("saving urls for september")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20161001" #yyyymmdd
end_date = "20161031" #yyyymmdd
print("saving urls for october")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20161101" #yyyymmdd
end_date = "20161130" #yyyymmdd
print("saving urls for november")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

begin_date = "20161201" #yyyymmdd
end_date = "20161231" #yyyymmdd
print("saving urls for december")

#new yor times only only allows upto 100 pages
for x in range(1, 101):
	dataparser(end_date, begin_date, sort, x)

with open('nytimes_articles_urls_jul_dec.json', 'w') as outfile:  
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