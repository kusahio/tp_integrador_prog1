def mostrar_estadisticas(paises):
    """Muestra estadísticas básicas de los países."""
    if not paises:
        print("No hay datos cargados.")
        return

    pais_mayor_pob = max(paises, key=lambda x: x["poblacion"])
    pais_menor_pob = min(paises, key=lambda x: x["poblacion"])
    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\nESTADÍSTICAS:")
    print(f"- País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']})")
    print(f"- País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']})")
    print(f"- Promedio de población: {promedio_pob:,.0f}")
    print(f"- Promedio de superficie: {promedio_sup:,.0f}")

    # Cantidad de países por continente
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\nCantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")