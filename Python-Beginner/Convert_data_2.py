# Convertir una lista en una cadena

students = ["Max", "Monika", "Erik", "Franziska"]

# Separador: agregar algo específico entre los elementos
# ¿Qué se debe agregar? "#", los elementos se concatenan mediante .join() y ¿qué se debe concatenar? la lista Students
print("#".join(students))

# El resultado se verá así: Max#Monika#Erik#Franziska

# Si ahora se desea tener comas entre los elementos, simplemente reemplace "#" con ","
students_as_string = ", ".join(students)


# Salida
print("En nuestra universidad estudian: " + students_as_string)


# Convertir una cadena en una Lista

# Dividir una cadena que luego se convierte en una lista


i = "Max, Monika, Erik, Franziska"
# Se divide con .split() (donde se divide, se determina con ", ")
print(i.split(", "))

# Otro Ejemplo

s = "Yo soy una oracion con muchas palabras"
print(s.split(" "))
# ¿Cuantos elementos hay en las lista?
print(len(s.split(" ")))
