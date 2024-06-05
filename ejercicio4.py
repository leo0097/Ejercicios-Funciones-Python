# Desarrollar un programa que solicite dos números en consola e imprima el resultado
# de las cuatro operaciones aritméticas aplicadas sobre ellos. Por ejemplo (en rojo la
# entrada del usuario):
# Escribe un número: 6
# Escribe otro número: 3
# a+b: 9
# a-b: 3
# a*b: 18
# a / b: 2
# Al final de la ejecución, mostrar un mensaje que nos advierta que el proceso ha
# terminado.
# Debemos tener en cuenta lo siguiente:
# • Si el usuario ingresa cualquier otro caracter que no sea un número,
# debe volver a preguntar, en ambos casos.
# • Tener en cuenta que el segundo número puede ser cero y, por ende,
# llegado el momento de la división el programa debe imprimir “No se
# puede dividir por cero”.
def solicitar_numero(num):
    while True:
        try:
            numero = int(input(num))
            return numero
        except ValueError:
            print("Error: ingrese un numero.")
a = solicitar_numero("Escribe un número: ")
b = solicitar_numero("Escribe otro número: ")
suma = a + b
resta = a - b
multiplicacion = a * b
if b != 0:
    division = a / b
else:
    division = "No se puede dividir por cero"

print(f"a + b: {suma}")
print(f"a - b: {resta}")
print(f"a * b: {multiplicacion}")
print(f"a / b: {division}")

print("Proceso terminado.")
