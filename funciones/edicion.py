import csv
import os

def guardar_pais(ruta_archivo, pais):
    try:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

        with open(ruta_archivo, mode='a', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writerow(pais)
        return True
    
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    except Exception as e:
        print(f"\nAVISO: Error al guardar en CSV - {e}")
        return False
    
def agregar_pais(paises, pais, ruta_archivo):
    try:
        if not isinstance(pais, dict):
            raise TypeError('El país debe ser un diccionario')
        
        if guardar_pais(ruta_archivo, pais):
            paises.append(pais)
            return True
        return False
        
    except (ValueError, TypeError) as e:
        print(f"\nAVISO: {e}")
        return False
    
def editar_pais():
    pass
