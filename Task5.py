from Task4 import*

def get_movie_list_details(movies_list):
#task 9
        random_time = random.randint(2,3)
        print (random_time)
        a =  time.sleep(random_time)
        all_movie_list = []
        for i in movies_list[:20]:
                url = i['url']
                movies_detail_list = scrape_movie_details(url)
                all_movie_list.append(movies_detail_list)
        return all_movie_list

all_detail = get_movie_list_details(scrept)
# print (all_detail)  