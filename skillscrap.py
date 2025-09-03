
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
response = requests.get('https://justjoin.it/job-offers/all-locations/testing')
soup = BeautifulSoup(response.content, 'html.parser')
content_div = soup.find('script', type= 'application/ld+json')
content_div = content_div.text
content_div = content_div.replace('<script type="application/ld+json"> {"@context":"https://schema.org","@type":"CollectionPage","name":"Job Offers","hasPart": ' , '').replace(']}</script>', ']')
print(content_div)
content_div = json.loads(content_div)



print(content_div)
