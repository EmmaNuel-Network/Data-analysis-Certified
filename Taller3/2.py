def desclonador(ls):
 
    new_list = []

    for i in ls:
        for j in ls[1:len(ls) - 1]:
            if i == j:
                pass
            elif i not in new_list:
                new_list.append(i)

    return new_list
                

ls = [0,0,1,1,2,3]

print(desclonador(ls))


