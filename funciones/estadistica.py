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
        try:
            pais_mayor_pob = max(paises, key=lambda x: x['poblacion'])
            pais_menor_pob = min(paises, key=lambda x: x['poblacion'])

        # Verifica que el nombre de la llave exista
        except KeyError as e:
            print(f'Error: Algunos países no tienen el campo {e}')
            return
        
        # Verifica que tipo de dato sea numérico
        except TypeError:
            print('Error: Los valores de población deben ser numéricos')
            return
        
        # Cálculo de promedios
        try:
            promedio_pob = sum(pais['poblacion'] for pais in paises) / len(paises)
            promedio_sup = sum(pais['superficie'] for pais in paises) / len(paises)

        # Verifica que el nombre de la llave exista
        except KeyError as e:
            print(f'Error: Algunos países no tienen el campo requerido ({e})')
            return
        
        # Verifica que tipo de dato sea numérico
        except TypeError:
            print('Error: Los valores de población o superficie deben ser numéricos')
            return
        
        # Error que arroja en caso de que la lista sea vacía, ya que no se puede dividir por 0
        except ZeroDivisionError:
            print('Error: No hay países para calcular promedios')
            return
        
        # Mostrar estadísticas básicas
        try:
            print('\n==== ESTADÍSTICAS ==== ')
            print(f'- País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})')
            print(f'- País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})')
            print(f'- Promedio de población: {promedio_pob:,.0f}')
            print(f'- Promedio de superficie: {promedio_sup:,.0f}')

        # Verifica que los nombres de campo existan 
        except KeyError as e:
            print(f'Error: Faltan campos {e} en algunos países')
            return
        
        # Cantidad de países por continente
        try:
            continentes = {}
            for pais in paises:
                cont = pais['continente']
                continentes[cont] = continentes.get(cont, 0) + 1
            
            print('\nCantidad de países por continente:')
            for cont, cant in continentes.items():
                print(f'  - {cont}: {cant}')

        # Verifica que el nombre de la llave exista
        except KeyError as e:
            print('Error: Algunos países no tienen el campo {e}')
            return
        # Error genérico que pudiera ocurrir
        except Exception as e:
            print(f'Error al agrupar por continentes: {e}')
            return
    # Error genérico que pudiera ocurrir
    except Exception as e:
        print(f'Error inesperado en mostrar_estadisticas: {e}')
        return