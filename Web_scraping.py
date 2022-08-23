#import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_titles = []
company_name = []
location_names = []
work_time_place = []
links = []

#2nd step is to use requests to url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=navbg")

#3rd step is to save page content
src = result.content
#print(src)

#4th step is create soup object
soup = BeautifulSoup(src, "lxml")
#print(soup)

#5th find the elements you need ins site web....
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_name = soup.find_all("a", {"class": "css-17s97q8"})
location_names = soup.find_all("span", {"class": "css-5wys0k"})
work_time_place = soup.find_all("span", {"class": "css-1ve4b75 eoyjyou0"})

# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_titles.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_name[i].text)
    location_names.append(location_names[i].text)
    work_time_place.append(work_time_place[i].text)


# 7th step create csv file
file_list = [job_titles, company_name, location_names, work_time_place, links]
exported = zip_longest(*file_list)
with open("/Users/BVS/PycharmProjects/SNAKEGAME/scrap.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job titles","company name", "location names", "work time and places", "links"])
    wr.writerows(exported)