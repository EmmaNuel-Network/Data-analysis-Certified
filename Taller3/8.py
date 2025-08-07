#Dado un diccionario de productos con sus precios, escribe un programa que convierta el 
#diccionario en una lista de tuplas, donde cada tupla contenga el producto y su precio. 


dicci = {
    "Arroz" : 1,
    "Papa"  : 2,
    "Huevo" : 0.5,
    "Pc Gamer" : 500,
    "Quantum Computer" : 10000000000000
}

ls = list(dicci.items())
    


print(type(ls))
print(ls)