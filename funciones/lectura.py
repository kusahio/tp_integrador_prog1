import csv  # leer/escribir archivos CSV (datos tabulares)
import os   # manejar archivos, rutas y carpetas del sistema

"""
funciones nativas usadas:
    raise: Sirve para lanzar una excepción (error) de forma manual
"""

# Leer csv
def leer_csv(ruta_archivo):
    paises = []
    
    try:
        # Si no encuentra el archivo en la ruta
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
        
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
                except (KeyError, ValueError) as e:
                    print(f"Error en fila: {e}")
        
        print(f"Se cargaron {len(paises)} países")
    
    # Maneja el error en el caso de que no encuentre el archivo
    except FileNotFoundError as e:
        print(f"Error: {e}")

    # Maneja errores de permisos de archivo o carpeta
    except PermissionError:
        print(f"Error: Sin permisos para leer {ruta_archivo}")

    # Maneja cualquier otro error genérico inesperado
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return paises