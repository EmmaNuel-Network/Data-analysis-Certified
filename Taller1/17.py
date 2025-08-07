a = int(input("Ingrese el primer número:\n"))
b = int(input("Ingrese el segundo número:\n"))

if a>b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")

else:
    print("Son iguales")