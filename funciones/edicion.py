import csv
import os

def guardar_pais(ruta_archivo, pais):
    try:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

        with open(ruta_archivo, mode='a', encoding='utf-8', newline='') as archivo:
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

def guardar_paises(ruta_archivo, paises):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escribir = csv.DictWriter(archivo, fieldnames=campos)
            escribir.writeheader()
            escribir.writerows(paises)
        
        return True
    
    except (PermissionError, OSError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    except Exception as e:
        print(f"\nAVISO: Error al guardar cambios en CSV - {e}")
        return False

    
def agregar_pais(paises, pais, ruta_archivo):
    try:
        if not isinstance(paises, list):
            raise TypeError('El elemento no es una lista')
        if not isinstance(pais, dict):
            raise TypeError('El país debe ser un diccionario')
        if guardar_pais(ruta_archivo, pais):
            paises.append(pais)
            return True
        return False
        
    except (ValueError, TypeError) as e:
        print(f"\nAVISO: {e}")
        return False
    
def editar_campo_pais(paises, indice, campo, nuevo_valor, ruta_archivo):

    try:
        if not (0 <= indice < len(paises)):
            raise ValueError(f"Índice {indice} fuera de rango")
        
        if campo not in ['nombre', 'poblacion', 'superficie', 'continente']:
            raise ValueError(f"Campo '{campo}' no válido")
        
        if campo in ['poblacion', 'superficie']:
            if not isinstance(nuevo_valor, int) or nuevo_valor <= 0:
                raise ValueError(f"El campo '{campo}' debe ser un número entero positivo")
        elif campo in ['nombre', 'continente']:
            if not isinstance(nuevo_valor, str) or not nuevo_valor.strip():
                raise ValueError(f"El campo '{campo}' debe ser un texto válido")
        
        # Guardar valor anterior
        valor_anterior = paises[indice][campo]
        
        paises[indice][campo] = nuevo_valor

        if guardar_paises(ruta_archivo, paises):
            print(f"\nCampo '{campo}' actualizado correctamente\n")
            print(f"  Anterior: {valor_anterior}")
            print(f"  Nuevo   : {nuevo_valor}")
            return True
        else:
            # Si falla al guardar, revertir el cambio en memoria
            paises[indice][campo] = valor_anterior
            print("\nNo se pudieron guardar los cambios en el archivo")
            return False
    
    except (ValueError, TypeError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    except Exception as e:
        print(f"\nAVISO: Error inesperado - {e}")
        return False
    