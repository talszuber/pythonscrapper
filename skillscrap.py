
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import csv
from csv import writer

def grab_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('script', type= 'application/ld+json')
    content_div = content_div.text
    content_div = content_div.replace('<script type="application/ld+json"> {"@context":"https://schema.org","@type":"CollectionPage","name":"Job Offers","hasPart": ' , '').replace(']}', ']')
    content_div = content_div.replace('{"@context":"https://schema.org","@type":"CollectionPage","name":"Job Offers","hasPart":', '').replace('', '')
    content_div = content_div.replace('</script>', '')
    content_div = json.loads(content_div)

    return content_div


url = input('enter section of justjoin.it (e.g. python, java, testing, or all):')

content_div = grab_jobs(url)

offer_amounts = len(content_div)

i = 0
d = 0
with open('job_list.csv', 'r') as f:
    csvreader = csv.reader(f)
    job_list = list(csvreader)
    print(job_list)
while i  < offer_amounts:
    offer = content_div[i]
    url = offer['url']

    if any(f'{url.split('/')[-1]}' in s for s in job_list):
        d += 1
        print(f'Duplicate no: {d}')
    else:
        response = urllib.request.urlopen(url)
        response_API = requests.get('https://api.justjoin.it/v1/offers/*id*'.replace('*id*', url.split('/')[-1]))
        response_json = response_API.json()
        slug = response_json['slug']
        slug = slug.replace('"',' ')
        title = response_json['title']
        title = title.replace('"',' ')
        exp = response_json['experienceLevel']['label']
        exp = exp.replace('"',' ')
        required_skills = response_json['requiredSkills']
        required_skills = str(required_skills)
        required_skills = required_skills.replace('name','').replace('}','').replace('{','').replace('[','').replace(']','').replace('"','').replace('level','lvl').replace(':','')
        nth_skills = response_json['niceToHaveSkills']
        nth_skills = str(nth_skills)
        nth_skills = nth_skills.replace('name','').replace('}','').replace('{','').replace('[','').replace(']','').replace('"','').replace('level','lvl').replace(':','')


        with open('job_list.csv', 'a', encoding='utf-8', newline='') as f:
            csvwriter = writer(f)
            csvwriter.writerow([slug, title, exp, required_skills, nth_skills])
            f.close()
        print(f'New entry: {i}')
    i += 1
print('Done')