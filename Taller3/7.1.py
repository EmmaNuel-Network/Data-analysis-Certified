import re

txt = "MIs queridos alumnos, es un placer para mi anunciarles el retiro de la tiranía de la autoridad"

new_text = re.split("[ , ,]",txt)

print(len(new_text))
print(new_text)