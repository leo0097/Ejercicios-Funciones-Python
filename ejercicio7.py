# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión. -
# En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos
# y dos espacios entre palabras " ".
# - El alfabeto morse soportado será el mostrado
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', 
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def texto_a_morse(palabra):
    morse = []
    for caracter in palabra.upper():
        if caracter in morse_dict:
            morse.append(morse_dict[caracter])
    return ' '.join(morse)

def morse_a_texto(morse):
    palabra = []
    for codigo in morse.split():
        for key, value in morse_dict.items():
            if value == codigo:
                texto.append(key)
    return ''.join(palabra)

def detectar_tipo_entrada(entrada):
    if any(char in morse_dict for char in entrada):
        return 'morse'
    else:
        return 'palabra'

def main():
    entrada = input("Ingrese una palabra o el código Morse: ")

    tipo = detectar_tipo_entrada(entrada)

    if tipo == 'palabra':
        morse = texto_a_morse(entrada)
        print("palabra convertido a código Morse:", morse)
    elif tipo == 'morse':
        palabra = morse_a_texto(entrada)
        print("Código Morse convertido a texto:", palabra)
    else:
        print("Entrada no válida.")

if __name__ == "__main__":
    main()
