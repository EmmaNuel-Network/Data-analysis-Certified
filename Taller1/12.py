#Cuente la cantidad de espacios en blanco hay en la siguiente frase: "Los 
#campistas necesitan practicar mucho con python!, por eso, harán bastantes 
#ejercicios!".

word =  "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!"
counter = 0
for i in word:
    if i == " ":
        counter +=1

print(f"EL numero de espacios en la palabras es de {counter}")