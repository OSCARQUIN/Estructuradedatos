print("==============bienvenidos a mis estructura de datos================")

#estructura de datos 
#listas
numeros = [1,2,3,4,5,6, 'Oscar carquin', True, 10, 11, 12]
# las listas son mutables
# si permiten valosres duplicados

print (numeros)
numeros.append("Carquin")
print("===================despues de agregar========================")
print(numeros)

print(numeros[6])
print("===================despues de meter un valor========================")
numeros[6] = 19
print(numeros)
numeros.remove(2)
print("===================despues de eliminar========================")
print(numeros)

#tupla
numeros = [1,2,3,4,5,6, 'Oscar carquin', True, 10, 11]
#las listas son inmutable
#si permiten valores duplicados


#conjuntos
numeros = [1,2,3,4,5,6, 'Oscar carquin', True, 10, 11]


#Diccionarios
personas = [
    persona1 = {
        "nombre" : "Oscar Carquin",
        "Edad"   : 31
        "ciudad" : "Lima",
        "correo" : "carquin2292@gmail.com"

    }
]