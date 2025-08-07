def mysorted(ls, begining=False):

    new_ls = []
    away = 1
    long = len(ls)
    
    while away <= long:

        max = ls[0]  # Tomar el primer elemento como referencia

        for i in range(1, len(ls)):  # Recorrer la lista para encontrar el mayor o menor
            if  begining == False:  # Si se ordena de menor a mayor
                if max > ls[i]:
                    max = ls[i]
            elif begining == True:  # Si se ordena de mayor a menor
                if max < ls[i]:
                    max = ls[i]
    
        new_ls.append(max)  # Agregar el elemento encontrado a la nueva lista
        away += 1
        ls.remove(max)  # Eliminarlo de la lista original para continuar con la ordenación
    
    return new_ls
def fuller(number):
    ls = []
    for i in range(0, number):
        item = int(input(f"Ingrese el dato # {i} :\n"))
        ls.append(item)

    return ls


print("""                                 Bienvenid@
Gracias por Usar el ordenador de Datos UltraMax109075 km hypersonic atomic Destroyer
La mejor Herramienta para ordenar su información ...
................................................
................................................
................................................
................................................
.............................................................""")

number = int(input("Ingrese la cantidad de elementos que desea ingresar:\n"))
ls  = fuller(number)

new_list = ["Datos Incorrecto, Vuelva y ejecute el programa"]

quest  = int(input("\nDesea organizarlo de formas Ascendente (opción 1) o Descendente (opción 2) en valor?:\n "))
if quest == 1:
    new_list  = mysorted(ls,False)
elif quest == 2:
    new_list  =  mysorted(ls,True)
else: 
    print("Escriba bien pedazo de loca")

print(new_list)