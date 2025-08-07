phrase = input("Ingrese la frase que desea concer su número de (a)s:\n")

counter = 0
for i in phrase:
    i.lower()
    if i == "a":
        counter = counter + 1
print(f"El número de letras (a) en la frase es de {counter}")