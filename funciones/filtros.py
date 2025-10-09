def buscar_pais(paises, nombre):
    """Busca países por coincidencia parcial o exacta."""
    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]
    return resultados


def filtrar_por_continente(paises, continente):
    """Filtra países por continente."""
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_rango(paises, campo, minimo, maximo):
    """Filtra países por un rango de valores (población o superficie)."""
    return [p for p in paises if minimo <= p[campo] <= maximo]