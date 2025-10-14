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
            
            for numero_fila, fila in enumerate(lector, start=2):  # start=2 porque la fila 1 es el encabezado
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except KeyError as e:
                    print(f"\nAVISO: Falta el campo {e} en la fila {numero_fila}")
                except ValueError as e:
                    print(f"\nAVISO: Valor inválido en la fila {numero_fila} - {e}")
        
        print(f"Se cargaron {len(paises)} países correctamente")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"\nAVISO: {e}")
    except Exception as e:
        print(f"\nAVISO: {e}")
    
    return paises