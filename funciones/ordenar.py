"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Sirve para verificar el tipo de dato de una variable u objeto
    raise: Sirve para lanzar una excepción (error) de forma manual
"""

# Ordena países por una clave dada (nombre, población, superficie)
def ordenar_paises(paises, clave, descendente=False):
    try:
        # Verificar que paises sea una lista
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        
        # Verificar que la lista no esté vacía
        if not paises:
            print("Advertencia: La lista de países está vacía")
            return []
        
        # Verificar que clave sea un string
        if not isinstance(clave, str):
            raise TypeError("El parámetro 'clave' debe ser un string")
        
        # Verificar que clave no esté vacía
        if not clave.strip():
            raise ValueError("El parámetro 'clave' no puede estar vacío")
        
        # Verificar que descendente sea booleano
        if not isinstance(descendente, bool):
            raise TypeError("El parámetro 'descendente' debe ser True o False")
        
        # Verificar que la clave existe en todos los países
        claves_validas = {"nombre", "poblacion", "superficie", "continente"}
        if clave not in claves_validas:
            raise ValueError(f"Clave inválida. Use una de: {', '.join(claves_validas)}")
        
        # Verificar que todos los países tengan la clave
        for i, pais in enumerate(paises):
            if not isinstance(pais, dict):
                raise TypeError(f"El elemento en la posición {i} no es un diccionario")
            
            if clave not in pais:
                raise KeyError(f"El país en la posición {i} no tiene la clave '{clave}'")
        
        # Ordenar los países
        paises_ordenados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
        
        return paises_ordenados
    
    except (TypeError, ValueError, KeyError, Exception) as e:
        print(f"\nAviso: {e}")
        return []