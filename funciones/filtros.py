from .utilidades import quitar_tildes

"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Sirve para verificar el tipo de dato de una variable u objeto
    raise: Sirve para lanzar una excepción (error) de forma manual
"""
# Busca países por coincidencia parcial o exacta
def buscar_pais(paises, nombre):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        # Se utiliza una "list comprehension" para iterar sobre la lista y filtrar
        resultados = [pais for pais in paises if quitar_tildes(nombre.lower()) in quitar_tildes(pais["nombre"].lower())]
        return resultados
    
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'nombre'")
        return []
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return []

#Filtra países por continente
def filtrar_por_continente(paises, continente):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(continente, str):
            raise TypeError("El parámetro 'continente' debe ser un string")
        
        return [pais for pais in paises if quitar_tildes(pais["continente"].lower()) == quitar_tildes(continente.lower())]
    
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'continente'")
        return []
    
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return []

# Filtra países por un rango de valores (población o superficie)
def filtrar_por_rango(paises, campo, minimo, maximo):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(campo, str):
            raise TypeError("El parámetro 'campo' debe ser un string")
        # if minimo > maximo:
        #     raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        
        return [pais for pais in paises if minimo <= pais[campo] <= maximo]
    
    except KeyError:
        print(f"\nAVISO: Algunos países no tienen el campo '{campo}'")
        return []

    except (TypeError, ValueError) as e:
        print(f"\nAVISO: {e}")
        return []

def buscar_exacto(paises, nombre):
    try:
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        # Buscar coincidencia exacta
        for pais in paises:            
            if quitar_tildes(nombre.lower().strip()) == quitar_tildes(pais["nombre"].lower().strip()):
                return pais
        return None
    
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'nombre'")
        return None
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return None