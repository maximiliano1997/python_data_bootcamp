# ¿Cómo elimino el último elemento de una lista?
# La función .pop() elimina la última entrada

planetas = ["Mercurio", "Venus", "Tierra", "Marte",
            "Júpiter", "Saturno", "Urano", "Neptuno", "Pluto"]
planetas.pop()
print(planetas)

# .pop() también devuelve algo (valor de retorno)
planetas = ["Mercurio", "Venus", "Tierra", "Marte",
            "Júpiter", "Saturno", "Urano", "Neptuno", "Pluto"]

p = planetas.pop()  # elimina el último elemento y lo almacena en una variable
print(p)
