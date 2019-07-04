from Task5 import* 
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
pprint.pprint (gener_analysis)
