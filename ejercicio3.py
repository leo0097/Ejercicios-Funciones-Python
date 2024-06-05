# Escriba un programa que pida la anchura y altura de un rectángulo y el caracter a
# utilizar en el dibujo.
def dibujar_rectangulo(ancho, alto,caracter):
    for i in range(alto):
        if i == 0 or i == alto - 1:
            print(caracter * ancho)
        else:
            print(caracter + ' ' * (ancho - 2) + caracter)
anchura = int(input("Ingrese el ancho de un rectangulo: "))
altura = int(input("Ingrese el alto del rectángulo: "))
caracter = input("ingrese un caracter para que tenga la forma el rectangulo ")
dibujar_rectangulo(anchura, altura,caracter)