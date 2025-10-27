"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Sirve para verificar el tipo de dato de una variable u objeto
    raise: Sirve para lanzar una excepción (error) de forma manual
"""

# Ordena países por una clave dada (nombre, población, superficie)

def ordenar_paises(paises, clave, descendente=False):
    try:
        # Verifica que 'paises' sea una lista
        if not isinstance(paises, list):
            raise TypeError("El parámetro 'paises' debe ser una lista")
        
        # Si la lista está vacía, informa y retorna lista vacía
        if not paises:
            print("Advertencia: La lista de países está vacía")
            return []
        
        # Verifica que 'clave' sea un string
        if not isinstance(clave, str):
            raise TypeError("El parámetro 'clave' debe ser un string")
        
        # Verifica que 'clave' no esté vacía o solo con espacios
        if not clave.strip():
            raise ValueError("El parámetro 'clave' no puede estar vacío")
        
        # Verifica que 'descendente' sea booleano
        if not isinstance(descendente, bool):
            raise TypeError("El parámetro 'descendente' debe ser True o False")
        
        # Valida que la clave esté entre las permitidas
        claves_validas = {"nombre", "poblacion", "superficie", "continente"}
        if clave not in claves_validas:
            raise ValueError(f"Clave inválida. Use una de: {', '.join(claves_validas)}")
        
        # Verifica que todos los elementos sean diccionarios y contengan la clave
        for i, pais in enumerate(paises):
            if not isinstance(pais, dict):
                raise TypeError(f"El elemento en la posición {i} no es un diccionario")
            if clave not in pais:
                raise KeyError(f"El país en la posición {i} no tiene la clave '{clave}'")
        
        # Ordena la lista por la clave indicada; 'reverse=True' para descendente
        paises_ordenados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
        
        # Devuelve la nueva lista ordenada (no modifica la original)
        return paises_ordenados
    
    # Cualquier problema de tipos, valores o claves faltantes se captura aquí
    except (TypeError, ValueError, KeyError, Exception) as e:
        print(f"\nAviso: {e}")
        return []