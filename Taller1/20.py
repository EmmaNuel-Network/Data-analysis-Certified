# Capturar el peso y la altura de una persona
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar la categoría del IMC
if imc < 18.5:
    categoria = "Desnutrición"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostrar el resultado
print(f"El IMC es: {imc:.2f}")
print(f"La categoría es: {categoria}")
