# Muestra estadísticas básicas de los países
def mostrar_estadisticas(paises):
    try:
        # Validación inicial
        if not paises:
            print('No hay datos cargados.')
            return
        
        if not isinstance(paises, list):
            raise TypeError('El parámetro "paises" debe ser una lista')
        
        # Cálculo de país con mayor y menor población
        pais_mayor_pob = max(paises, key=lambda x: x['poblacion'])
        pais_menor_pob = min(paises, key=lambda x: x['poblacion'])
        
        # Cálculo de promedios
        promedio_pob = sum(pais['poblacion'] for pais in paises) / len(paises)
        promedio_sup = sum(pais['superficie'] for pais in paises) / len(paises)
        
        # Mostrar estadísticas básicas
        print('\n==== ESTADÍSTICAS ==== ')
        print(f'- País con mayor población  : {pais_mayor_pob["nombre"]} ({pais_mayor_pob["poblacion"]:,})')
        print(f'- País con menor población  : {pais_menor_pob["nombre"]} ({pais_menor_pob["poblacion"]:,})')
        print(f'- Promedio de población     : {promedio_pob:,.0f}')
        print(f'- Promedio de superficie    : {promedio_sup:,.0f}')
        
        # Cantidad de países por continente
        continentes = {}
        for pais in paises:
            cont = pais['continente']
            continentes[cont] = continentes.get(cont, 0) + 1
        
        print('\nCantidad de países por continente:')
        for cont, cant in continentes.items():
            print(f'  - {cont}: {cant}')
    
    except KeyError as e:
        print(f'\nAVISO: Algunos países no tienen el campo {e}')
    except (TypeError, ValueError) as e:
        print(f'\nAVISO: {e}')
    except ZeroDivisionError:
        print('\nAVISO: No hay países para calcular promedios')
    except Exception as e:
        print(f'\nAVISO: {e}')