print("""     CÁLCULADORA AÑO BISIESTO   """)
year  = int(input("Ingrese el año que desea analizar:\n"))

c = bool

if year % 4 == 0:
    if year % 100 != 0:
       c = True
    elif year % 100 == 0 and year % 400 == 0:
       c = True 
    else:
        c = False
else:
   c = False



if c == True:
    print(f"El año {year} es un Año Bisiesto...")
else:
    print(f"El año {year} NO es un Año Bisiesto...")
