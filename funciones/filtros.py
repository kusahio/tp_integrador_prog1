
from .utilidades import quitar_tildes

"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Verifica el tipo de dato de una variable u objeto.
    raise: Lanza una excepción (error) de forma manual.
"""

# Busca países por coincidencia parcial o exacta en el nombre
def buscar_pais(paises, nombre):
    try:
        # Validaciones de tipo de parámetros
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        # List comprehension: filtra países cuyo nombre contenga el texto buscado (ignorando tildes y mayúsculas)
        resultados = [
            pais for pais in paises
            if quitar_tildes(nombre.lower()) in quitar_tildes(pais["nombre"].lower())
        ]
        return resultados
    
    # Algún país no tiene la clave 'nombre'
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'nombre'")
        return []
    # Tipos inválidos o métodos de string usados sobre objetos no-string
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return []

# Filtra países por continente (coincidencia exacta, normalizando tildes y mayúsculas)
def filtrar_por_continente(paises, continente):
    try:
        # Validaciones de tipo
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(continente, str):
            raise TypeError("El parámetro 'continente' debe ser un string")
        
        # Devuelve los países cuyo continente coincide exactamente con el solicitado (normalizado)
        return [
            pais for pais in paises
            if quitar_tildes(pais["continente"].lower()) == quitar_tildes(continente.lower())
        ]
    
    # Algún país no tiene la clave 'continente'
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'continente'")
        return []
    # Tipos inválidos o atributos de string faltantes
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return []


# Filtra países por un rango numérico (para 'poblacion' o 'superficie')
def filtrar_por_rango(paises, campo, minimo, maximo):
    try:
        # Validaciones de tipo de parámetros
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(campo, str):
            raise TypeError("El parámetro 'campo' debe ser un string")
        # Validación opcional: rango consistente (descomenta si querés forzarlo)
        # if minimo > maximo:
        #     raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        
        # Retorna países cuyo valor en 'campo' esté dentro del rango [minimo, maximo]
        return [pais for pais in paises if minimo <= pais[campo] <= maximo]
    
    # El campo no existe en algún país
    except KeyError:
        print(f"\nAVISO: Algunos países no tienen el campo '{campo}'")
        return []
    # Tipos inválidos o comparación no permitida (por ejemplo, valores no numéricos)
    except (TypeError, ValueError) as e:
        print(f"\nAVISO: {e}")
        return []


# Busca coincidencia exacta por nombre (ignorando tildes y mayúsculas)
def buscar_exacto(paises, nombre):
    try:
        # Validaciones de tipo
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        # Recorre la lista y compara el nombre normalizado (exacto)
        for pais in paises:
            if quitar_tildes(nombre.lower().strip()) == quitar_tildes(pais["nombre"].lower().strip()):
                return pais
        # Si no hay coincidencia exacta, retorna None
        return None
    
    # Algún país no tiene la clave 'nombre'
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'nombre'")
        return None
    # Tipos inválidos o atributos de string faltantes
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return None



# Filtra países por continente
def filtrar_por_continente(paises, continente):
    try:
        # Validación de tipos de parámetros
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(continente, str):
            raise TypeError("El parámetro 'continente' debe ser un string")
        
        # Compara el continente normalizando tildes y mayúsculas/minúsculas
        return [
            pais for pais in paises
            if quitar_tildes(pais["continente"].lower()) == quitar_tildes(continente.lower())
        ]
    
    # Algún diccionario no tiene la clave 'continente'
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'continente'")
        return []
    # Tipos incorrectos o intento de usar métodos de string en valores no-string
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return []


# Filtra países por un rango de valores (por ejemplo, 'poblacion' o 'superficie')
def filtrar_por_rango(paises, campo, minimo, maximo):
    try:
        # Validación de tipos básicos
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(campo, str):
            raise TypeError("El parámetro 'campo' debe ser un string")
        
        # Devuelve los países cuyo valor para 'campo' está dentro del rango [minimo, maximo]
        return [pais for pais in paises if minimo <= pais[campo] <= maximo]
    
    # Falla si el diccionario no incluye la clave indicada por 'campo'
    except KeyError:
        print(f"\nAVISO: Algunos países no tienen el campo '{campo}'")
        return []
    # Tipos no válidos o comparaciones no permitidas (p.ej., valores no numéricos)
    except (TypeError, ValueError) as e:
        print(f"\nAVISO: {e}")
        return []

# Busca un país por coincidencia exacta del nombre (ignorando tildes y mayúsculas)
def buscar_exacto(paises, nombre):
    try:
        # Validaciones de tipo de parámetros
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        if not isinstance(nombre, str):
            raise TypeError("El parámetro 'nombre' debe ser un string")
        
        # Recorre la lista y compara el nombre normalizado (lower + sin tildes + strip)
        for pais in paises:
            if quitar_tildes(nombre.lower().strip()) == quitar_tildes(pais["nombre"].lower().strip()):
                return pais
        # Si no encuentra coincidencia exacta, devuelve None
        return None
    
    # Falla si algún país no tiene la clave 'nombre'
    except KeyError:
        print("\nAVISO: Algunos países no tienen el campo 'nombre'")
        return None
    # Tipos incorrectos o uso de métodos de string sobre valores no-string
    except (TypeError, AttributeError) as e:
        print(f"\nAVISO: {e}")
        return None