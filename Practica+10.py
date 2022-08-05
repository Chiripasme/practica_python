#Cadenas en Python.

nombre = "marco {}"
edad = 34
nombres = """Marco
luis 
rosa 
carlos
"""

#Trabajar con una cadena.
for x in nombre:
    print(x)

print(len(nombre))
print(nombre * 3)

#Cortar cadenas.

print(nombre[0:2])

#Cadenas y sus metodos: upper(), lower(), replace(), format()

print(nombre.upper())
print(nombre.lower())
print(nombre.replace("C", "p"))
print(nombre.format(edad))