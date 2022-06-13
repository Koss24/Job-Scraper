
from bs4 import BeautifulSoup
import requests


URL_BASE = 'https://ca.indeed.com'

jobtitle = input('Enter your search query: ')
jobtitle = jobtitle.replace(' ', '%20')
jobtitle = jobtitle + '%20'
print(jobtitle)
#content = requests.get('https://ca.indeed.com/jobs?q&l=Canada&from=searchOnHP&vjk=b5990b4a839cf016').text
content = requests.get('https://ca.indeed.com/jobs?q='+ f'{jobtitle}&l=Canada&' + 'start=0&vjk=baafa75344c2ff23').text
print('https://ca.indeed.com/jobs?q='+ f'{jobtitle}&l=Canada&' + 'start=0&vjk=baafa75344c2ff23')
soup = BeautifulSoup(content, 'html.parser')
jobCards = soup.find_all('div', class_ = 'cardOutline')



count = 0

#loop all all the job outlines that are found on the first page
for job in jobCards:
    count += 1
    '''
    The Title, location, company name and salary (if placed on ad)
    can be scraped directly off the jobcard
    '''
    title = job.find('h2', class_ = 'jobTitle').text
    location = job.find('div', class_ = 'companyLocation').text
    companyName = job.find('span', class_ = 'companyName').text
    try: 
        salary = job.find('div', class_= 'attribute_snippet').text
    except:
        print('No salary Found\n\n\n\n')
        salary = 'N/A'
        
    '''
    to get the job description we generate the url for the current job card
    '''
    getUrl = job.find(href=True)
    url = getUrl['href']
    listing = requests.get(URL_BASE + f'{url}').text
    
    #listing = requests.get('https://ca.indeed.com/viewjob?jk=f48302af45ec233c&l=Canada&from=web&advn=5410671297569085&adid=391097008&ad=-6NYlbfkN0B4M_22gisP5C23iXLOHQc82nqiv9jWCiHfA12bXM_A1-85GZV13nMpoXvY4znr4U36JzP1RafSC0_f2I-rAX_Offrvv8KPQZGo5JsOKgG5TORy3x41xXKnxABcoJnNeelwxs0YvrDaQdDnKMr6KoB7MzH_dme1f1WzSWhO1g_K2fqAURmbZNw4bRR5x3sqQ0WIZEQ9SjEHdlX9ARHhhsCRanGMcX8xfnH1ebKrONaPBYwN-8oa-kkwF_lAJ4ckUnWPtPN0sgQaaqSS6wQ9qGfF8O6Xd22lATGxUkI_K9YtebBmHp4rncq4KiajpZjMbdGotTxWJUSwAErA_oT9Jue07kXAg1KqsaioIj2-SXDLpOV1o4UWKEhI&pub=4a1b367933fd867b19b072952f68dceb&vjs=3').text
    print(title)
    print(location)
    print(salary)
    soup2 = BeautifulSoup(listing,'html.parser')
    print(URL_BASE + f'{url}')
    job_desription = soup2.find('div', class_ = 'jobsearch-JobComponent-description icl-u-xs-mt--md')
    jobText = job_desription.find('div', 'jobsearch-jobDescriptionText').text
    if count == 1:
        break;


''''
title = jobCard[1].find('h2', class_ = 'jobTitle').text
url = jobCard[0].find(href=True)
x = url['href']


test = requests.get('https://ca.indeed.com' + f'{x}')
print('https://ca.indeed.com' + f'{x}')
'''