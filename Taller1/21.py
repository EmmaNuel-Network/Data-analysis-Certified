# Capturar el estrato y el salario del empleado
estrato = int(input("Ingrese el estrato del empleado (1-6): "))
salario = float(input("Ingrese el salario del empleado: "))

# Calcular el bono según el estrato
if estrato == 1:
    bono = salario * 0.35
elif estrato == 2:
    bono = salario * 0.30
elif estrato == 3:
    bono = salario * 0.25
elif estrato == 4:
    bono = salario * 0.20
elif estrato in [5, 6]:
    bono = salario * 0.10
else:
    bono = 0
    print("Estrato no válido.")

# Calcular el total a pagar
total_a_pagar = salario + bono

# Mostrar el resultado
print(f"El bono de temporada es: {bono:.2f}")
print(f"El total a pagar es: {total_a_pagar:.2f}")
