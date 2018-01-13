import newspaper
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

#Bluemix Credentials
pi_username = "c6a0e689-0186-42ed-be38-4713c469465e"
pi_password = "W5TmbS4o7XQN"

personality_insights = PersonalityInsights(username=pi_username, password=pi_password)


# cnn_paper = newspaper.build('http://cnn.com/politics') #takes a minute

# for category in cnn_paper.category_urls():
# 	print(category)

# for article in cnn_paper.articles:
# 	print(article.url)


url = 'https://www.nytimes.com/2017/05/22/us/politics/michael-flynn-fifth-amendment-russia-senate.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news&_r=0'

a = newspaper.Article(url)
a.download()
a.parse()

a_text = a.text
a_text = a_text.encode('utf-8')
print(a.text)
print("\n")
print(a.authors)
print("\n")

personality = personality_insights.profile(a_text)
print(personality)
