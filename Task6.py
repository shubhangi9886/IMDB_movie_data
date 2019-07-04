from Task5 import*
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
pprint.pprint (language_count)