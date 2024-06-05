# Escribe una función que reciba un texto y retorne verdadero o falso (Boolean)
# según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a
# derecha que de derecha a izquierda. NO se tienen en cuenta los espacios, signos de
# puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
def es_palindromo(texto):
    texto_limpio = ''.join(texto.split())

    return texto_limpio == texto_limpio[::-1]
texto_usuario = input("Ingrese el texto a verificar si es un palindromo: ")
if es_palindromo(texto_usuario.replace(" ", "")):
    print("El texto es un palindromo.")
    print("Texto invertido:", texto_usuario[::-1])
else:
    print("El texto no es un palindromo.")

