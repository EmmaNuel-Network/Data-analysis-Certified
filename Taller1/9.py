name = input("Ingrese su nombre completo:\n")

name_splited = name.split(" ")

name = map(str.capitalize, name_splited)

name = " ".join(name)


print(name)

