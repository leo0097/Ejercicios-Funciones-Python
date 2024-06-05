# Crea una función que evalúe si un/a atleta ha superado correctamente una carrera
# de obstáculos.
# - La función recibirá dos parámetros:
# - Un array que sólo puede contener String con las palabras "run" o "jump"
# - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
# - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
# será correcto y no variará el símbolo de esa parte de la pista.
# - Si hace "jump" en "_" (suelo), se variará la pista por "x".
# - Si hace "run" en "|" (valla), se variará la pista por "/". - 
# La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.
def evaluar_carrera(tipo_carrera):
    if tipo_carrera not in ["run", "jump"]:
        print("Error: Tipo de carrera no válido.")
        return False
    if tipo_carrera == "jump":
        pasos = ["_", "|", "_", "|"]
        acciones_esperadas = ["run", "jump", "run", "jump"]
    else:
        pasos = ["_", "_", "_"]
        acciones_esperadas = ["run", "run", "run"]
    for paso, accion_esperada in zip(pasos, acciones_esperadas):
        print(f"Paso {paso}: {paso}")
        accion_usuario = input(f"Ingrese la acción del atleta para el paso {paso} ({accion_esperada}): ").lower()
        if accion_usuario != accion_esperada:
            print("El atleta cometió un error. La carrera no ha sido superada correctamente.")
            return False
    print("¡El atleta ha superado correctamente la carrera!")
    return True
tipo_carrera = input("Ingrese el tipo de carrera (run o jump): ").lower()
evaluar_carrera(tipo_carrera)

