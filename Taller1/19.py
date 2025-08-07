salario = float(input("Ingrese el salario de la persona: "))

SMMLV = 1000000
salario_integral = 10 * SMMLV

if salario >= salario_integral:
    print("El salario es integral.")
else:
    print("El salario no es integral.")
