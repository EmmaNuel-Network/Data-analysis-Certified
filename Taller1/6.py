import math

choose = input("Especifique si el angulo que ingresará está en radianes o grados:\n")
angulo = int(input("Ingrese el Ángulo:\n"))

if choose == "grados":
    angulo = math.radians(angulo)

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f""""Las trigonométricas del angulo {angulo} en {choose} son:
      seno {sen}, coseno {cos}, tan {tan}.""")


