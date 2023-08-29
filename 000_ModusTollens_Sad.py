print("Modus Tollens Edad para votar"+"\n\n")

# Definimos una regla de inferencia
def es_elegible_para_votar(TF):
    if TF == 1:
        return True
    else:
        return False

# Pedimos la edad al usuario
TF = int(input("Es usted apto para votar? \nNo=0, Si=1\n"))

# Aplicamos la regla de inferencia
if es_elegible_para_votar(TF):
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")
