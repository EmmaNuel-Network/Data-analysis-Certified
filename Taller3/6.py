ls = [1,3,8,7,9,0,1000,-1]

max = 0
min = max

away = 0
long = len(ls)


for j in ls:
    if max < j:
        max = j
    if min > j:
        min = j


print(f"maximus is: {max} and minimus is: {min}")