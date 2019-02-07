from bs4 import BeautifulSoup

import requests

"""
Author : Navneet Chandra Tiwari
Email: navneet058@gmail.com
Website:

Note : This program is for educational purpose

"""

url="http://www.example.com"

r = requests.get(url)

soup = BeautifulSoup(r.content,'lxml')

total_css_links=[]

tag_list=['a','div','table','ul','img','span','label']

for search_tag in tag_list:
    for element in soup.find_all(search_tag):
        if element.get('style') is not None:
            #print(element)
            total_css_links.append(element)
            

print(len(total_css_links))
