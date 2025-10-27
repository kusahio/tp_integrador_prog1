# Muestra estadísticas básicas de los países

def mostrar_estadisticas(paises):
    try:
        # Validación inicial: lista vacía
        if not paises:
            print('No hay datos cargados.')
            return
        
        # Validación de tipo: debe ser una lista
        if not isinstance(paises, list):
            raise TypeError('El parámetro "paises" debe ser una lista')
        
        # Cálculo del país con mayor y menor población
        # Usa las claves del diccionario 'poblacion' para comparar
        pais_mayor_pob = max(paises, key=lambda x: x['poblacion'])
        pais_menor_pob = min(paises, key=lambda x: x['poblacion'])
        
        # Cálculo de promedios (población y superficie) sobre toda la lista
        promedio_pob = sum(pais['poblacion'] for pais in paises) / len(paises)
        promedio_sup = sum(pais['superficie'] for pais in paises) / len(paises)
        
        # Mostrar estadísticas básicas con formato de miles
        print('\n==== ESTADÍSTICAS ==== ')
        print(f'- País con mayor población  : {pais_mayor_pob["nombre"]} ({pais_mayor_pob["poblacion"]:,})')
        print(f'- País con menor población  : {pais_menor_pob["nombre"]} ({pais_menor_pob["poblacion"]:,})')
        print(f'- Promedio de población     : {promedio_pob:,.0f}')
        print(f'- Promedio de superficie    : {promedio_sup:,.0f}')
        
        # Conteo de países por continente
        continentes = {}
        for pais in paises:
            cont = pais['continente']
            # Incrementa el contador del continente (inicializa en 0 si no existe)
            continentes[cont] = continentes.get(cont, 0) + 1
        
        # Muestra el desglose por continente
        print('\nCantidad de países por continente:')
        for cont, cant in continentes.items():
            print(f'  - {cont}: {cant}')
    
    # Faltan claves esperadas en algún país (e.g., 'poblacion', 'superficie', 'continente' o 'nombre')
    except KeyError as e:
        print(f'\nAVISO: Algunos países no tienen el campo {e}')
    # Tipos no válidos en la estructura de datos o en operaciones aritméticas
    except (TypeError, ValueError) as e:
        print(f'\nAVISO: {e}')
    # Protección extra (en teoría el len() ya previene división por cero)
    except ZeroDivisionError:
        print('\nAVISO: No hay países para calcular promedios')
    # Cualquier otro error no contemplado
    except Exception as e:
        print(f'\nAVISO: {e}')