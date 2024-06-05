# Escribir una función que reciba una muestra de números en una lista y devuelva su
# media.
def calcular_media():
    cantidad_numeros = int(input("cuantos numero se van a ingresar para calcular la media: "))
    numeros = []
    for i in range(cantidad_numeros):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    
    if len(numeros) == 0:
        return 0  
    else:
        media = sum(numeros) / len(numeros)
        return media
media_resultado = calcular_media()
print("La media de los números ingresados es:", media_resultado)