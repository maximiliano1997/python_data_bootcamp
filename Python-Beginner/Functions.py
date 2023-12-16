# Función

def multi_print(nombre):
    print(nombre)
    print(nombre)


multi_print("HALLO")
multi_print("WELT")


def multi_counter(nombre, contador):
    for i in range(contador):
        print(nombre)


multi_counter("Hola", 5)

# Las funciones pueden contener funciones


def multi_function():
    multi_counter("Hola", 3)
    multi_counter("Mundo", 3)


multi_function()

# return para seguir trabajando con el resultado
# Valor de retorno


def maximo(a, b):
    if a < b:
        return b
    else:
        return a


resultado = maximo(1, 5)
print(resultado)
