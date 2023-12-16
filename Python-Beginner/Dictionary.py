# Diccionarios en Python
# - Puedes almacenar asignaciones de valores (por ejemplo, una guía telefónica: un apellido tiene un número de teléfono)
# - Puedes modificar / eliminar / agregar elementos posteriormente en un diccionario
# - Realmente necesitarás diccionarios una y otra vez

# Los diccionarios tienen Clave y Valor
# CLAVE: VALOR
# Una clave está conectada, por así decirlo, con un valor y eso sucede con : (dos puntos)
d = {"Berlín": "BER", "Helsinki": "HEL", "Saigón": "SGN"}
print(d)
# Salida: {'Berlín': 'BER', 'Helsinki': 'HEL', 'Saigón': 'SGN'}
print(d["Helsinki"])
# Con un índice [] y el nombre de la cadena, puedes acceder a la clave y obtener el valor
# Comprueba si hay un valor asociado a la entrada Helsinki
# Salida: HEL

# # Agregar una entrada
# d["Budapest"] = "BUD"
# print(d)
# # Salida: {'Berlín': 'BER', 'Helsinki': 'HEL', 'Saigón': 'SGN', 'Budapest': 'BUD'}

# # Eliminar una entrada
# del d["Budapest"]
# print(d)
# # Salida: {'Berlín': 'BER', 'Helsinki': 'HEL', 'Saigón': 'SGN'}
# # Elimina la entrada y el valor asociado BUD

# # Comprobación: ¿Está un elemento en el diccionario?
# if "Budapest" in d:
#     print("Budapest está en el diccionario")
# if "Saigón" in d:
#     print("Saigón está en el diccionario")
# # Salida: "Saigón está en el diccionario"

# # Acceder a un elemento:
# print(d["Saigón"])
# print(d.get("Saigón"))
# # Salida: ambas líneas imprimen SGN
# # Pero generalmente es mejor usar [] en lugar de .get() ya que el programa se interrumpe con .get() y es mejor para informar errores

# Diccionario y bucles

# d = {"Munich": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

# for key in d:
#     value = d[key]
#     print(key)
#     print(value)

# # Salida
# # Munich
# # MUC
# # Budapest
# # BUD
# # Helsinki
# # HEL

# # Mostrar todos los valores en el diccionario como una especie de lista con tuplas
# print(d.items())
# # Salida
# # dict_items([('Munich', 'MUC'), ('Budapest', 'BUD'), ('Helsinki', 'HEL')])
# # ¡Esto no es realmente una lista!

# for key, value in d.items():
#     print(key + ": " + value)

# # Salida
# # Munich: MUC
# # Budapest: BUD
# # Helsinki: HEL
