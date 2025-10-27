import csv  # leer/escribir archivos CSV (datos tabulares)
import os   # manejar archivos, rutas y carpetas del sistema

'''
funciones nativas usadas:
    raise: Sirve para lanzar una excepción (error) de forma manual
'''

# Crear CSV
def crear_csv(ruta_archivo):
    try:
        # Verifica que la ruta recibida sea un string
        if not isinstance(ruta_archivo, str):
            raise TypeError('El parámetro "ruta_archivo" debe ser un string')
        
        # Obtiene el directorio donde se guardará el archivo
        directorio = os.path.dirname(ruta_archivo)
        
        # Si el directorio no existe, se crea
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f'Se creó el directorio: {directorio}')
        
        # Crea el archivo CSV y escribe la fila de encabezados
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            # Define los nombres de las columnas
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
        
        # Mensajes informativos
        print(f'Se creó el archivo CSV en: {ruta_archivo}')
        print(f'  Campos: {", ".join(campos)}')
        return True
    
    # Sin permisos para escribir en la ruta indicada
    except PermissionError:
        print(f'\nAVISO: No se tienen permisos para crear el archivo en: {ruta_archivo}')
        return False
    
    # Errores del sistema de archivos (ruta inválida, disco lleno, etc.)
    except OSError as e:
        print(f'\nAVISO: Error del sistema al crear el archivo - {e}')
        return False
    
    # Cualquier otro error inesperado
    except Exception as e:
        print(f'\nAVISO: Error inesperado al crear el archivo - {e}')
        return False


# Leer csv
def leer_csv(ruta_archivo, crear_si_no_existe=True):
    # Lista donde se acumularán los países leídos del CSV
    paises = []
    
    try:
        # Si el archivo no existe en la ruta indicada
        if not os.path.exists(ruta_archivo):
            if crear_si_no_existe:
                # Informa y ofrece crear el archivo vacío con encabezados
                print(f'\nNo se encontró el archivo: {ruta_archivo}')
                print('\nAVISO: Creando archivo CSV')
                
                # Intenta crear el archivo; si se logra, retorna lista vacía
                if crear_csv(ruta_archivo):
                    print('\n El archivo está vacío. Puedes agregar países manualmente.')
                    return []
                else:
                    # Si falla la creación, se lanza error para manejar abajo
                    raise FileNotFoundError(f'No se pudo crear el archivo: {ruta_archivo}')
            else:
                # Si no se debe crear automáticamente, se lanza error
                raise FileNotFoundError(f'No se encontró el archivo: {ruta_archivo}')
        
        # Abre el archivo y prepara un lector de diccionarios
        with open(ruta_archivo, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            # Recorre las filas a partir de la 2 (1 es encabezado)
            for numero_fila, fila in enumerate(lector, start=2):  # start=2 porque la fila 1 es el encabezado
                try:
                    # Construye el dict del país validando y transformando tipos
                    pais = {
                        'nombre': fila["nombre"].strip(),
                        'poblacion': int(fila["poblacion"]),
                        'superficie': int(fila["superficie"]),
                        'continente': fila["continente"].strip()
                    }
                    # Agrega a la lista acumulada
                    paises.append(pais)
                # Faltan columnas esperadas en el CSV
                except KeyError as e:
                    print(f'\nAVISO: Falta el campo {e} en la fila {numero_fila}')
                # Error al convertir datos a int u otros valores inválidos
                except ValueError as e:
                    print(f'\nAVISO: Valor inválido en la fila {numero_fila} - {e}')
        
        # Mensaje de resumen luego de la carga
        if len(paises) != 0:
            print(f'Se cargaron {len(paises)} países correctamente')
        else:
            print("El CSV no tiene datos, ingrese datos.")
    
    # Errores comunes de acceso/archivo
    except (FileNotFoundError, PermissionError) as e:
        print(f'\nAVISO: {e}')
    # Cualquier otro error no contemplado
    except Exception as e:
        print(f'\nAVISO: {e}')
    
    # Devuelve la lista (puede estar vacía si no había datos)
    return paises