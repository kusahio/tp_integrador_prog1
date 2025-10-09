import csv
import os

def leer_csv(ruta_archivo):
    paises = []
    if not os.path.exists(ruta_archivo):
        print(f"No se encontró el archivo: {ruta_archivo}")
        return paises

    with open(ruta_archivo, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                paises.append(pais)
            except (KeyError, ValueError):
                print(f"Error en el formato de la fila: {fila}")
    return paises