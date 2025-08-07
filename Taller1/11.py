#Solicite el ingreso de una palabra y una letra, luego diga en qué posición 
#está la letra que usted indicó. 

word = input("Ingrese la palabra:\n")
let = input("¿Cuál letra desea conocer su primera posición?:\n")

print(f"La letra {let} se encuentra en la posición {word.index(let)} de la palabras {word}")
