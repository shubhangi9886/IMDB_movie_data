from Task1 import*

def scrape_movie_details(movie_url1):
        movie_details_dic = {}
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
                runtime_minites = int(movie_runtime[1:].strip('min'))
                movie_runtime = runtime_hours + runtime_minites
        else:
                movie_runtime = runtime_hours
                
                gener = sub_div.find_all('a')
                gener.pop()
                movie_gener = [i.get_text()for i in gener]
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
                                        movie_language = [language.get_text() for language in tag_anchor]
                                elif 'Country:' in text:
                                        tag_anchor = div.find_all('a')
                                        movie_country = ''.join([country.get_text() for country in tag_anchor])
                        movie_poster_link  = soup.find('div', class_ ="poster").a['href']
                movie_details_dic['name'] = movie_name
                movie_details_dic['director'] = movie_directors
                movie_details_dic['bio'] = movie_bio
                movie_details_dic['runtime'] =movie_runtime
                movie_details_dic['gener'] = movie_gener
                movie_details_dic['language'] = movie_language
                movie_details_dic['country'] = movie_country
                movie_details_dic['poster_img_url'] = movie_poster_link
        return movie_details_dic
        
movie_url1 =  scrept[0]['url']
movie_detail = scrape_movie_details(movie_url1)
# pprint.pprint (movie_detail) 
