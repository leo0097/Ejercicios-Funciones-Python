# Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con
# caracteres producto (*)

def dibujar_rectangulo(ancho, alto):
    for i in range(alto):
        if i == 0 or i == alto - 1:
            print('*' * ancho)
        else:
            print('*' + ' ' * (ancho - 2) + '*')
anchura = int(input("Ingrese el ancho de un rectangulo: "))
altura = int(input("Ingrese el alto del rectángulo: "))
dibujar_rectangulo(anchura, altura)
