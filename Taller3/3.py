ls = [1,2,4,5,6,7,8,9,10]

def sumaPar(ls):
    suma_pares = 0

    for j in ls:
        if j % 2 == 0:
            suma_pares += j
    return suma_pares


print(sumaPar)