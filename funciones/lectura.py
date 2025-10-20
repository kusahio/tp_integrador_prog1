import csv  # leer/escribir archivos CSV (datos tabulares)
import os   # manejar archivos, rutas y carpetas del sistema

'''
funciones nativas usadas:
    raise: Sirve para lanzar una excepción (error) de forma manual
'''

def crear_csv(ruta_archivo):
    try:
        # Verificar que la ruta sea un string
        if not isinstance(ruta_archivo, str):
            raise TypeError('El parámetro "ruta_archivo" debe ser un string')
        
        # Obtener el directorio donde se creará el archivo
        directorio = os.path.dirname(ruta_archivo)
        
        # Si el directorio no existe, crearlo
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f'Se creó el directorio: {directorio}')
        
        # Crear el archivo CSV con los encabezados
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            # Definir los campos del CSV
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            
            # Crear el escritor CSV
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribir la fila de encabezados
            escritor.writeheader()
        
        print(f'Se creó el archivo CSV en: {ruta_archivo}')
        print(f'  Campos: {", ".join(campos)}')
        return True
    
    except PermissionError:
        print(f'\nAVISO: No se tienen permisos para crear el archivo en: {ruta_archivo}')
        return False
    
    except OSError as e:
        print(f'\nAVISO: Error del sistema al crear el archivo - {e}')
        return False
    
    except Exception as e:
        print(f'\nAVISO: Error inesperado al crear el archivo - {e}')
        return False

# Leer csv
def leer_csv(ruta_archivo, crear_si_no_existe=True):
    paises = []
    
    try:
        # Si no encuentra el archivo en la ruta
        if not os.path.exists(ruta_archivo):
            if crear_si_no_existe:
                print(f'\nNo se encontró el archivo: {ruta_archivo}')
                print('\nAVISO: Creando archivo CSV')
                
                if crear_csv(ruta_archivo):
                    print('\n El archivo está vacío. Puedes agregar países manualmente.')
                    return []
                else:
                    raise FileNotFoundError(f'No se pudo crear el archivo: {ruta_archivo}')
            else:
                raise FileNotFoundError(f'No se encontró el archivo: {ruta_archivo}')
        
        with open(ruta_archivo, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for numero_fila, fila in enumerate(lector, start=2):  # start=2 porque la fila 1 es el encabezado
                try:
                    pais = {
                        'nombre': fila["nombre"].strip(),
                        'poblacion': int(fila["poblacion"]),
                        'superficie': int(fila["superficie"]),
                        'continente': fila["continente"].strip()
                    }
                    paises.append(pais)
                except KeyError as e:
                    print(f'\nAVISO: Falta el campo {e} en la fila {numero_fila}')
                except ValueError as e:
                    print(f'\nAVISO: Valor inválido en la fila {numero_fila} - {e}')
        if len(paises) != 0:
            print(f'Se cargaron {len(paises)} países correctamente')
        else:
            print("El CSV no tiene datos, ingrese datos.")
    except (FileNotFoundError, PermissionError) as e:
        print(f'\nAVISO: {e}')
    except Exception as e:
        print(f'\nAVISO: {e}')
    
    return paises