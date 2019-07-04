from Task2 import*

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
pprint.pprint(group_by_decade(dec_arg))