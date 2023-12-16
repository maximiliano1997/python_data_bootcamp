# # Definicion de estudiantes
# estudiante1 = "Max"
# estudiante2 = "Imanol"
# estudiante3 = "Lucas"
# estudiante4 = "Maksim"

# # Creacion de una Lista de Estudiantes
# estudiantes = ['Max', "Imanol", "Lucas", "Maksim"]
# print(estudiantes)

# # Agregar nuevos Estudiantes a la lista existente usando .append
# estudiantes.append('Santino')
# print(estudiantes)

# # Calcular la cantidad de elementos en la lista con len (len esuna funcion)
# print(len(estudiantes))

# # Impimir el ultimo elemento en una lista usando [-1]
# print(estudiantes[-1])

# # Imprimir varios strings concatenados
# print(estudiantes[0] + ' & ' + estudiantes[-1])


# # Eliminar una entrada especifica en tu lista
# # Se puede eliminar una entrada con un indice especifico usando del

# print(estudiantes[3])
# del estudiantes[3]
# print(estudiantes)


# # Eliminar sin índice usando .remove() cuando se sabe exactamente qué se debe eliminar
# estudiantes.remove("Santino")
# print(estudiantes)

# # Slicing de lista
# print(estudiantes[:])  # Con [:] se crea una copia de la lista
# # [1:] omite el elemento en la posición 1 y muestra todos los demás
# print(estudiantes[1:])
# # Desde el índice 1 hasta exclusivamente el último elemento
# print(estudiantes[1:-1])
# print(estudiantes[:-1])  # Todos los elementos excepto el último


# # El Slicing también funciona para cadenas de texto
# print("Hallo Welt"[0:5])  # Salida: Hallo
# print("Hallo Welt"[-4:])  # Muestra los últimos 4 caracteres

# # El Slicing se inicia con [:] - antes del : donde quiero comenzar
# #                                  - después del : dónde debo terminar


# # Ejemplo:
# # Salida: Welt -> Comienza después de la posición 6, es decir, W, y termina en el último elemento, en este caso, t.
# print("Hallo Welt"[6:-1])


#######################################################
# Comprensión de listas
# Sintaxis: nueva_lista = [expresión for elemento in iterable if condición == True]
# Se puede agregar una instrucción if si es necesario, pero también se puede omitir
xs = [1, 2, 3, 4, 5, 6, 7, 8]

# Normalmente escribiríamos algo como esto:
# ys = []
# for x in xs:
#     ys.append(x)
# Con la comprensión de listas, podemos hacerlo más corto
ys = [x * x for x in xs]
print(ys)
# Salida: [1, 4, 9, 16, 25, 36, 49, 64]
# Lo que hace: crea una lista, declara la variable al principio e itera a través de la lista mientras usa un bucle for

# Otro ejemplo:
frutas = ["manzana", "plátano", "cereza", "kiwi", "mango"]

nueva_lista = [x for x in frutas if "a" in x]
# Crea una lista, itera a través de la lista 'frutas' y verifica si hay una 'a' en x
print(nueva_lista)
# Salida: ['manzana', 'plátano', 'mango']
