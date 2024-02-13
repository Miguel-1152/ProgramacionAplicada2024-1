#################LISTAS####################
###########################################

my_lista = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde", ]

#input()
print(my_lista)
print(type(my_lista))
print(my_lista[2]) #Imprime el segundo espacio de la lista desde el 0 

print("my_lista size:", len(my_lista))
print(my_lista[0:2]) #los primeros 2 espacios de la lista
print(my_lista[ :2]) #2 en 2


my_lista.append("Blanco") #Agregar elemento al final de la lista 
print(my_lista)


my_lista.insert(3, 'Negro') #Agregar elemento en el espacio solicitado (3)
print(my_lista)


my_lista.extend(["Marron", "Gris"])   #Agrega a otra lista
print(my_lista)


print(my_lista.index("Azul")) #Indica la ubicación del elemento


#my_lista.remove("Magenta") 
my_lista.remove("Marron")  #Remover un elemento de la lista
print(my_lista)


my_lista.insert(8, "Marron")  #Agregar elemento en el espacio solicitado (8)
print(my_lista)


print(my_lista.pop())  #Imprime el ultimo elemento de la lista
size = len (my_lista)   #Se le asigna el tamaño de la lista a "size"
print("size=", size)
#print(my_lista.pop(size))


my_lista_3 = my_lista*3    #Se le asigna tres veces "my_lista" a "my_lista_3"
print("my_lista_3:", my_lista_3)


print("Sort:")
print()
my_listaSort = my_lista.sort()
print(my_listaSort)


my_Numlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordering my_Numlist:")
my_Numlist.sort()      #Ordena la lista de menor a mayor
print(my_Numlist)
#OrderedLList = my_Numlist.sort()
#print(my_listaSort)


#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)


#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple:", my_tupla)



print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento esta contenido en una tupla (devuelve un valor booleano)
print("Rojo" in my_tupla)
print(my_tupla.count("Rojo"))


#Tupla con un solo elemnto
my_tupla_unitaria = ("Blanco")
print(my_tupla_unitaria)


#Empaquetado de tupla, tupla sin parentesis
my_tupla ="Gaspar", 5, 8, 1999
print(my_tupla)


#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre:", nombre, "-Dia:", dia, "-Mes:", mes, "-Año", año)

#Convertir una tupla en una lista
my_lista_2=list(my_tupla)
print(my_lista_2)
"""