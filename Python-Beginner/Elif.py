# elif como una conexión entre else e if
# útil cuando se tienen múltiples bloques de else e if

moneda = "€"

if moneda == "$":
    print("Dólar estadounidense")
else:
    if moneda == "¥":
        print("Yen japonés")
    else:
        if moneda == "€":
            print("Euro")
        else:
            if moneda == "฿":
                print("Baht tailandés")
# Aquí se imprimirá Euro
# Esto se puede acortar usando Elif

moneda = "¥"

if moneda == "$":
    print("Dólar estadounidense")
elif moneda == "¥":
    print("Yen japonés")
elif moneda == "€":
    print("Euro")
elif moneda == "฿":
    print("Baht tailandés")

# Aqui se imprimira Yen japones
# # pero es más legible
