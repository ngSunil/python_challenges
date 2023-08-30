# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
#     1: Sort based on name
#     2: Then sort based on age
#     3: Then sort by score
# The priority is that name > age > score.

s_list = []
while True:
    s = input('Please enter the tupples: ')
    if not s:
        break
    else:
        s_list.append(tuple(s.split(',')))

s_list.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))
print(s_list)