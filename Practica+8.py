# FOR es para listas, tuplas y diccionarios.            
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Ejmplo de FOR con listas.
for x in dias:
   print(x)



# Ejemplo de FOR con BREAK.
for x in dias:
    print(x)
    if x == "viernes":
        break



# Ejemplo de FOR con Excepción.
for x in dias:
    if x == "viernes":
        break
    print(x)



# Ejemplo FOR de repeticion.
numero = 10
for x in range(numero):
    print("Hola")
else:
    print("Fin del ejemplo")

