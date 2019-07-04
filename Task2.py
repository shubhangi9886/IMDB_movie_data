from Task1 import*

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
pprint.pprint (dec_arg)