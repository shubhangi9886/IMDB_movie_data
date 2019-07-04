import requests
from bs4 import BeautifulSoup
import json
import pprint
import os
import time
import random
import pathlib


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

#Task 2

def group_by_year(movies):
    years = []
    for i in movies:
        year = i["year"]
        if year not in years:
            years.append(year)
    movies_dict = {i:[] for i in years}
    for i in movies:
        year = i['year']
        for x in movies_dict:
                if str(x) == str(year):
                        movies_dict[x].append(i)

       
    return (movies_dict)
dec_arg =  group_by_year(scrept)
# pprint.pprint (dec_arg)

#Task 3

def group_by_decade(movies):
    moviedec = {}
    new_list1 = []
    for index in movies:
        mod = index%10
        decade = index-mod
        if decade not in new_list1:
            new_list1.append(decade)
    new_list1.sort()
    for i in new_list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = i + 9
        for x in movies:
            if x <= dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
        with open("task2.json","w") as fs:
                json.dump(moviedec,fs,indent = 1)

    return(moviedec)
# pprint.pprint(group_by_decade(dec_arg))

# Task 12

def scrape_movie_cast(movie_url,movie_caste_url):
        a = movie_url.split("/")
        s =  a[5] 
        data_store = "movie_cast_detail/" + s + ".json"
        filepath = pathlib.Path(data_store)
        if filepath.exists():
                with open(data_store,"r") as json_data:
                        f = f.read()
                        # print f
                        data = json.loads(f)
                return data 
        else:
                print ("file exists nahi hai")
                cast_list = []
                url = url1 + "fullcredits?ref_=tt_cl_sm#cast"
                data1 = requests.get(url)
                soup = BeautifulSoup(data1.text,'html.parser')
                table_data = soup.find('table', class_="cast_list") 
                actors = table_data.find_all('td',class_ = "")
                for actor in actors:
                        actor_Dict = {} 
                        id_cast = actor.find('a').get('href')[6:15]
                        name = actor.find('a').get_text().strip()
                        actor_Dict['imdb_id'] = id_cast
                        actor_Dict['name'] = name  
                        cast_list.append(actor_Dict)

                data_store = "movie_cast_detail/" + s + "_cast.json"
                with open(data_store,"w") as data:
                        data.write(json.dumps(cast_list,data,indent=1))
        return cast_list
for j in scrept:
        url=j["url"]	
	url1=url
        # scrape_movie_cast(url,url1)

# Task 4
def scrape_movie_details(movie_url1):
        movie_details_dic = {}
        # Task 8
        movie_language = ""
        movie_country = ""
        movieId = ''
        for i in movie_url1[28:]:
                if '/' not in i:
                        movieId += i 
                else:
                        break
        data_store = "all_movie_detail/" + movieId + ".json"
        filepath = pathlib.Path(data_store)
        if filepath.exists():
                with open(data_store,"r") as json_data:
                        f = json_data.read()
                        data = json.loads(f)
                return data 
        else:
                print "nahi hai"
                page = requests.get(movie_url1)
                soup = BeautifulSoup(page.text,"html.parser")
                title_div = soup.find('div',class_ = "title_wrapper").h1.get_text().strip()
                movie_name = title_div.split()
                movie_name.pop()
                movie_name = ' '.join(movie_name)
                        
        sub_div = soup.find('div',class_ = "subtext")
        runtime = sub_div.find('time').get_text().strip()
        runtime_hours = int(runtime[0])*60
        if 'min' in sub_div:
                runtime_minites = int(movie_runtime[1:4].strip('min'))
                movie_runtime = runtime_hours + runtime_minites
                
        gerne = soup.find('div',class_ = 'subtext')
        a_tag = gerne.find_all('a')
        a_tag.pop()
        gerne_list = [i.get_text()for i in a_tag]
        summary = soup.find('div',class_ = "plot_summary_text")
        movie_bio = soup.find('div',class_="summary_text").get_text().strip()
        director = soup.find('div',class_ = "credit_summary_item")
        director_list = director.find_all('a')
        movie_directors = [i.get_text().strip()for i in director_list]
        extra_details =  soup.find('div',attrs = {"class":"article","id":"titleDetails"})
        list_of_divs = extra_details.find_all('div')
        for div in list_of_divs:
                tag_h4 = div.find_all('h4')
                for text in tag_h4:
                        if 'Language:' in text:
                                tag_anchor = div.find_all('a')
                                movie_language = ([language.get_text() for language in tag_anchor])
                        elif 'Country:' in text:
                                tag_anchor = div.find_all('a')
                                movie_country = ''.join([country.get_text() for country in tag_anchor])
                        elif 'Runtime:' in text:
                                run = div.find('time').get_text().strip()
                                movie_details_dic['runtime'] = run
                movie_poster_link  = soup.find('div', class_ ="poster").a['href']
                movie_poster = "https://www.imbd.com"+ movie_poster_link

                movie_details_dic['name'] = movie_name
                movie_details_dic['director'] = movie_directors
                movie_details_dic['bio'] = movie_bio
                movie_details_dic['gener'] = gerne_list
                movie_details_dic['poster'] = movie_poster
                movie_details_dic['language'] = movie_language
                movie_details_dic['country'] = movie_country
                movie_details_dic ['caste'] =  scrape_movie_cast(url,url1)
                # Task 8
                with open(data_store,"w") as file1:
                        file1.write(json.dumps(movie_details_dic,indent=1))
        return movie_details_dic
movie_url1 =  scrept[0]['url']
movie_detail = scrape_movie_details(movie_url1)
# pprint.pprint (movie_detail) 

# Task 5

def get_movie_list_details(movies_list):
#task 9
        random_time = random.randint(2,3)
        print (random_time)
        a =  time.sleep(random_time)
        all_movie_list = []
        for i in movies_list[:250]:
                url = i['url']
                movies_detail_list = scrape_movie_details(url)
                all_movie_list.append(movies_detail_list)
        return all_movie_list
all_detail = get_movie_list_details(scrept)
# pprint.pprint (all_detail)                

# # Task 6

def analyse_movies_language(movie_detail_lang):
        movie_dict = {}
        for i in movie_detail_lang:
                if i not in movie_dict:
                        movie_dict[i] = 1
                else:
                        movie_dict[i] +=1
        return  movie_dict
movie_language_detail = []
for i in all_detail:
        lang = i["language"]
        movie_language_detail.extend(lang)
language_count = analyse_movies_language(movie_language_detail) 
# pprint.pprint (language_count)

# #Task 7

def analyse_movies_directors(movie_detail_directors):
        movie_directors_detail = {}
        for i in movie_detail_directors:
                if i not in movie_directors_detail:
                        movie_directors_detail[i] = 1
                else:
                        movie_directors_detail[i] +=1
        return movie_directors_detail
movie_detail_of_directore = []
for i in all_detail:
        dire = i["director"]
        movie_detail_of_directore.extend(dire)
director_count = analyse_movies_directors(movie_detail_of_directore)
# pprint.pprint (director_count)

# #Task 10

def analyse_language_and_directors(movie_list):
        director_dict = {}
        for movie in movie_list:
                for director in movie['director']:
                        director_dict[director] = {}
        for i in range(len(movie_list)):
                for director in director_dict:
                        if director in movie_list[i]['director']:
                                for language in movie_list[i]['language']:
                                        director_dict[director][language] = 0
        for i in range(len(movie_list)):
                for director in director_dict:
                        if director in movie_list[i]['director']:
                                for language in movie_list[i]['language']:
                                        director_dict[director][language] += 1
        return director_dict
director_by_language = analyse_language_and_directors(all_detail)
# pprint.pprint (director_by_language)

# #Task 11
def analyse_movies_genre(movie_list):
        gener_dict = {}
        for movie in movie_list:
                for gener in movie['gener']:
                        if gener not in gener_dict:
                                gener_dict[gener] = 1
                        else:
                                gener_dict[gener] += 1
        return gener_dict
gener_analysis = analyse_movies_genre(all_detail)
# pprint.pprint (gener_analysis)


#Tast 15 
def analyse_actors(movies_detail_list):
    actors_total_movie = {}
    for i in movies_detail_list:
        jso_caste = i['caste']
        for j in jso_caste:
            caste_id = j['imdb_id']
            caste_name = j['name']
            if caste_id in actors_total_movie:
                dic['num_movie'] +=  1
            else:
                actors_total_movie[caste_id] = {}
                dic =  actors_total_movie[caste_id]
                dic['name'] = caste_name
                dic['num_movie'] = 1
    return  actors_total_movie     
pprint. pprint (analyse_actors(all_detail))