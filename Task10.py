from  Task5 import*
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
pprint.pprint (director_by_language)