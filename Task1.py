import requests
from bs4 import BeautifulSoup
import json
import pprint
import os
import time
import random

URL = "https://www.imdb.com/india/top-rated-indian-movies/"

def scrap_top_tist():
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"html.parser")

    tbody = soup.find('tbody',class_ = "lister-list")
    trs = tbody.findAll('tr')
    new_list = []
    j = 0
    for i in trs:
        new = {}
        position = j=j+1
        name = i.find('td',class_="titleColumn").a.get_text()
        year = i.find('td',class_="titleColumn").span.get_text()
        reng = i.find('td',class_="ratingColumn").get_text()
        link = i.find("td",class_="titleColumn").a["href"]
        movie_link = "https://www.imdb.com/"+link

        new['position']=position
        new['name']=name
        new['year']=int(year[1:5])
        new['reting']=float(reng)
        new['url']=movie_link
        
        new_list.append(new)
        
    return new_list

scrept = scrap_top_tist()
# pprint.pprint (scrept)