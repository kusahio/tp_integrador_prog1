import csv
import os


def guardar_pais(ruta_archivo, pais):
    try:
        # Verifica si el archivo existe en la ruta especificada
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    
        # Abre el archivo en modo 'append' para agregar datos al final
        with open(ruta_archivo, mode='a', encoding='utf-8', newline='') as archivo:
            # Define los nombres de las columnas del CSV
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            # Crea un escritor de diccionarios para escribir en formato CSV
            escribir = csv.DictWriter(archivo, fieldnames=campos)
            # Escribe una fila con los datos del país
            escribir.writerow(pais)
        return True
    
    # Maneja errores relacionados con el archivo (no encontrado, permisos, etc.)
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    # Captura cualquier otro error inesperado
    except Exception as e:
        print(f"\nAVISO: Error al guardar en CSV - {e}")
        return False



def guardar_paises(ruta_archivo, paises):
    try:
        # Verifica que 'paises' sea una lista
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        
        # Obtiene el directorio de la ruta y lo crea si no existe
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        
        # Abre el archivo en modo escritura para sobrescribir el contenido
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            # Define los nombres de las columnas del CSV
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            # Crea un escritor de diccionarios para escribir en formato CSV
            escribir = csv.DictWriter(archivo, fieldnames=campos)
            # Escribe la fila de encabezados
            escribir.writeheader()
            # Escribe todas las filas con los datos de la lista 'paises'
            escribir.writerows(paises)
        return True
    
    # Maneja errores relacionados con permisos o sistema de archivos
    except (PermissionError, OSError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    # Captura cualquier otro error inesperado
    except Exception as e:
        print(f"\nAVISO: Error al guardar cambios en CSV - {e}")
        return False

    

def agregar_pais(paises, pais, ruta_archivo):
    try:
        # Verifica que 'paises' sea una lista
        if not isinstance(paises, list):
            raise TypeError('El elemento no es una lista')
        # Verifica que 'pais' sea un diccionario con los datos a guardar
        if not isinstance(pais, dict):
            raise TypeError('El país debe ser un diccionario')
        
        # Intenta guardar el país en el CSV; si se guarda correctamente,
        # también lo agrega a la lista en memoria
        if guardar_pais(ruta_archivo, pais):
            paises.append(pais)
            return True
        
        # Si no se pudo guardar en el archivo, no modifica la lista
        return False
        
    # Maneja errores de tipo o de valor en las validaciones previas
    except (ValueError, TypeError) as e:
        print(f"\nAVISO: {e}")
        return False
    
def editar_campo_pais(paises, indice, campo, nuevo_valor, ruta_archivo):
    try:
        # Verifica que el índice esté dentro del rango de la lista
        if not (0 <= indice < len(paises)):
            raise ValueError(f"Índice {indice} fuera de rango")
        
        # Valida que el campo a modificar sea uno de los permitidos
        if campo not in ['nombre', 'poblacion', 'superficie', 'continente']:
            raise ValueError(f"Campo '{campo}' no válido")
        
        # Reglas de validación según el tipo de campo
        if campo in ['poblacion', 'superficie']:
            # Debe ser entero positivo
            if not isinstance(nuevo_valor, int) or nuevo_valor <= 0:
                raise ValueError(f"El campo '{campo}' debe ser un número entero positivo")
        elif campo in ['nombre', 'continente']:
            # Debe ser un string no vacío (quitando espacios)
            if not isinstance(nuevo_valor, str) or not nuevo_valor.strip():
                raise ValueError(f"El campo '{campo}' debe ser un texto válido")
        
        # Guarda el valor anterior para poder revertir en caso de error al persistir
        valor_anterior = paises[indice][campo]
        
        # Aplica el cambio en memoria
        paises[indice][campo] = nuevo_valor

        # Intenta persistir todos los países en el CSV
        if guardar_paises(ruta_archivo, paises):
            print(f"\nCampo '{campo}' actualizado correctamente\n")
            print(f"  Anterior: {valor_anterior}")
            print(f"  Nuevo   : {nuevo_valor}")
            return True
        else:
            # Si falló al guardar, revierte el cambio en memoria (operación atómica)
            paises[indice][campo] = valor_anterior
            print("\nNo se pudieron guardar los cambios en el archivo")
            return False
    
    # Manejo de errores por validaciones y tipos de datos
    except (ValueError, TypeError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    # Captura cualquier otro error inesperado
    except Exception as e:
        print(f"\nAVISO: Error inesperado - {e}")
        return False