import unicodedata

"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Sirve para verificar el tipo de dato de una variable u objeto
    raise: Sirve para lanzar una excepción (error) de forma manual
"""

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Busca países por coincidencia parcial o exacta
def buscar_pais(paises, nombre):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        resultados = [pais for pais in paises if quitar_tildes(nombre.lower()) in quitar_tildes(pais["nombre"].lower())]
        return resultados
    
    # Verifica que el nombre de la llave exista
    except KeyError:
        print("Error: Algunos países no tienen el campo 'nombre'")
        return []
    
    # Verifica que el nombre sea un string válido
    except AttributeError:
        print("Error: El nombre debe ser un string válido")
        return []
    
    # Captura cualquier otro error genérico no previsto
    except Exception as e:
        print(f"Error inesperado en buscar_pais: {e}")
        return []

#Filtra países por continente
def filtrar_por_continente(paises, continente):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(continente, str):
            raise TypeError("El parámetro 'continente' debe ser un string")
        
        return [pais for pais in paises if quitar_tildes(pais["continente"].lower()) == quitar_tildes(continente.lower())]
    
    # Verifica que el nombre de la llave exista
    except KeyError:
        print("Error: Algunos países no tienen el campo 'continente'")
        return []
    
    # Verifica que el continente sea un string válido
    except AttributeError:
        print("Error: El continente debe ser un string válido")
        return []
    
    # Captura cualquier otro error genérico no previsto
    except Exception as e:
        print(f"Error inesperado en filtrar_por_continente: {e}")
        return []

# Filtra países por un rango de valores (población o superficie)
def filtrar_por_rango(paises, campo, minimo, maximo):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(campo, str):
            raise TypeError("El parámetro 'campo' debe ser un string")
        if not isinstance(minimo, (int, float)) or not isinstance(maximo, (int, float)):
            raise TypeError("Los valores mínimo y máximo deben ser numéricos")
        if minimo > maximo:
            raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        
        return [pais for pais in paises if minimo <= pais[campo] <= maximo]
    
    # Verifica que el nombre de la llave exista
    except KeyError:
        print(f"Error: Algunos países no tienen el campo '{campo}'")
        return []
    
    # Si el valor del campo no es numérico y no se puede comparar o si los parámetros no son del tipo correcto
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return []
    
    # Captura cualquier otro error genérico no previsto
    except Exception as e:
        print(f"Error inesperado en filtrar_por_rango: {e}")
        return []