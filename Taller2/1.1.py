print("TABLA DE MULTIPLCIAR\n")
number = int(input("Ingrese el número el cual desea conocer sus Múltiplos hasta el 10:\n"))



rango = int(input("Ingrese la cantidad de cifras que desea conocer Y/N:\n"))


counter = 1
ls = []
while counter <= rango:
    multiplo = counter * number
    ls.append(multiplo)

    counter +=1

print("..Cálculos finalizados..\n")
print(f"Acontinuación, los Múltiplos de {number}\n")

for i in ls:
    print(i)



