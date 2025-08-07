print("SUMA DE PARES\n")
rango = int(input("Ingrese el rango en el cual se buscarán los páres a ser Sumados:\n"))

pares = [1]
for i in range(2,rango + 1):
    if i % 2 == 0:
        pares.append(i)

sum = 0
for i in pares:
    sum +=i

print(f"La suma de todos los números Páres entre el 1 y el {rango} es: {sum}")