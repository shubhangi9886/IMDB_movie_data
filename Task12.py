from Task1 import*

def scrape_movie_cast(id):
        a = id.split("/")
        s =  a[5] 
        file_name = s + '_cast.json'
        file_path = os.path.exists("/home/komal/WebScraping/movie_cast_detail/"+file_name)
        if file_path:
                with open("/home/komal/WebScraping/movie_cast_detail/"+file_name,'r') as f :
                        print ("file exists hai")
                        f = f.read()
                        # print f
                        data = json.loads(f)
                return data 
        else:
                print ("file exists nahi hai")
                cast_list = []
                url = cast_data + "fullcredits?ref_=tt_cl_sm#cast"
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
                with open("/home/komal/WebScraping/movie_cast_detail/"+file_name,"w") as f:
                        f.write(json.dumps(cast_list,f,indent=1))
        return cast_list
for j in scrept:
        cast_data = j['url']
        # print cast_data
        # scrape_movie_cast(cast_data)