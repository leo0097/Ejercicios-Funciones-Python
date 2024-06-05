# Crea una función “calcularMaxMin” que recibe una 
# lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida 
# números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def main():
    def solicitar_numeros(cantidad):
        numeros = []
        for i in range(cantidad):
            numero = float(input(f"Ingrese el numero {i + 1}: "))
            numeros.append(numero)
        return numeros

    def calcularMaxMin(lista):
        if len(lista) == 0:
            return None, None
        else:
            maximo = max(lista)
            minimo = min(lista)
            return maximo, minimo

    cantidad = int(input("Ingrese la cantidad de numeros que se van a analizar: "))
    numeros = solicitar_numeros(cantidad)
    maximo, minimo = calcularMaxMin(numeros)
    if maximo is None or minimo is None:
        print("No se ingresaron numeros.")
    else:
        print("El maximo es:", maximo)
        print("El mínimo es:", minimo)

if __name__ == "__main__":
    main()


