import csv
from bs4 import BeautifulSoup
import requests
import time


# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(str, input("\nEnter key : ").strip().split()))[:n]
unfamiliar_skill1 = a[0]
unfamiliar_skill2 = a[1]

print('Filtering out the results')


def find_jobs():
    source = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java&txtLocation=").text
    soup = BeautifulSoup(source, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        # job_title = job.h2.a.text
        job_title = job.find('header', class_='clearfix').h2.a.text
        company_name = job.h3.text.strip()
        # or company_name = job.find('h3', class_='joblist-comp-name').text

        published_date = job.find('span', class_="sim-posted").text

        more_info = job.find('header', class_='clearfix').h2.a['href']

        key_skills = job.find('span', class_='srp-skills').text.replace(" ", '')

        if unfamiliar_skill1 in key_skills:
            # if unfamiliar_skill2 in key_skills:
            print(job_title)
            print(key_skills)
            print(company_name)
            print(published_date)
            print(more_info)

        # if 'few' in published_date:
        #     print(published_date)


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)



