print("Modus Ponens Edad para votar"+"\n\n")

# Definimos una regla de inferencia
def es_elegible_para_votar(edad):
    if edad >= 18:
        return True
    else:
        return False

# Pedimos la edad al usuario
edad = int(input("Ingrese su edad: "))

# Aplicamos la regla de inferencia
if es_elegible_para_votar(edad):
    print("Usted es elegible para votar.")
else:
    print("Usted no es elegible para votar.")
