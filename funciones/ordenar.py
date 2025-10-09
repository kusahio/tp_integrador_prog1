def ordenar_paises(paises, clave, descendente=False):
    """Ordena países por una clave dada (nombre, población, superficie)."""
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)