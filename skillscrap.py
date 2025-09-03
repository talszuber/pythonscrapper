
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
from csv import writer
response = requests.get('https://justjoin.it/job-offers/all-locations/testing')
soup = BeautifulSoup(response.content, 'html.parser')
content_div = soup.find('script', type= 'application/ld+json')
content_div = content_div.text
content_div = content_div.replace('<script type="application/ld+json"> {"@context":"https://schema.org","@type":"CollectionPage","name":"Job Offers","hasPart": ' , '').replace(']}', ']')
content_div = content_div.replace('{"@context":"https://schema.org","@type":"CollectionPage","name":"Job Offers","hasPart":', '').replace('', '')
content_div = content_div.replace('</script>', '')
content_div = json.loads(content_div)
offer_amounts = len(content_div)

i = 0
#with open("offers_skills.csv", "a", newline="",encoding='utf-8-sig') as file:
while i  < offer_amounts:
#    writer_object = writer(file)
    offer = content_div[i]
    url = offer['url']
    response = urllib.request.urlopen(url)
    response_API = requests.get('https://api.justjoin.it/v1/offers/*id*'.replace('*id*', url.split('/')[-1]))
    response_json = response_API.json()
    title = response_json['title']
    company = response_json['companyName']
    required_skills = response_json['requiredSkills']
    nth_skills = response_json['niceToHaveSkills']
    exp = response_json['experienceLevel']['label']
    print(f' {title}, {exp}, {required_skills}, {nth_skills}')
#    writer_object.writerow(f'{title}, {company}, {exp}, {required_skills}, {nth_skills}')
    i += 1
print('Done')