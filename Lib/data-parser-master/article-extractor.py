import json
import requests
import newspaper
#import sources from sources.py
from sources import source_dict

print (source_dict)

#Build newspaper objects you can interact with - VERY SLOW LOCALLY
for i in source_dict:
	newspaper_name = i["name"]
	newspaper_url = i["url"]

	newspaper_name = newspaper.build(newspaper_url)

# the name is the variable used to refer to the newspaper object, creating a list with just names
source_list = []
for i in source_dict:
	for key, value in i.items():
		if key == "name":
			source_list.append(value)

print(source_list)

# #list article urls
# for article in