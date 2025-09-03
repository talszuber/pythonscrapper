
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import ast
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
while i  < offer_amounts:
    offer = content_div[i]
    print(offer['url'])

    i += 1

#print(offer_amounts)
