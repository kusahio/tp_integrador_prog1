def formatear_pais(pais, index, tipo_formato='simple'):
    '''    
    Args:
        pais (dict): Diccionario con información del país
        index (int): Número de índice a mostrar
        tipo_formato (str): Tipo de formato: 'simple', 'poblacion', 'superficie', 'completo'
    
    Ejemplos:
        formatear_pais({'nombre': 'Argentina', 'continente': 'América'}, 1, 'simple')
        → '  1. Argentina - América'
        
        formatear_pais({'nombre': 'Argentina', 'poblacion': 45000000}, 1, 'poblacion')
        → '  1. Argentina: 45,000,000 habitantes'
    '''
    # Formato con población
    if tipo_formato == 'poblacion':
        return f'  {index}. {pais['nombre']}: {pais['poblacion']:,} habitantes'
    
    # Formato con superficie
    elif tipo_formato == 'superficie':
        return f'  {index}. {pais['nombre']}: {pais['superficie']:,} km²'
    
    # Formato completo con toda la información
    elif tipo_formato == 'completo':
        return (f'  {index}. {pais['nombre']}\n      Continente: {pais['continente']}\n      Población: {pais['poblacion']:,} habitantes\n      Superficie: {pais['superficie']:,} km²')
    
    # Formato simple (por defecto)
    else:
        return f'  {index}. {pais['nombre']} - {pais['continente']}'


def mostrar_con_paginacion(resultados, items_por_pagina=10, titulo='Resultados', tipo_formato='simple'):
    '''    
    Ejemplo de uso:
        mostrar_con_paginacion(paises, titulo='Países encontrados')
        mostrar_con_paginacion(paises, tipo_formato='poblacion')
    '''

    # Verificar si hay resultados para mostrar
    if not resultados:
        print('\nNo hay resultados para mostrar.')
        return
    
    # Validar que items_por_pagina sea un número positivo
    # Si no lo es, usar 10 como valor por defecto
    if not isinstance(items_por_pagina, int) or items_por_pagina <= 0:
        items_por_pagina = 10

    # Contar cuántos items hay en total
    total_items = len(resultados)

    # Ejemplo: 25 items, 10 por página → (25 + 9) // 10 = 3 páginas
    total_paginas = (total_items + items_por_pagina - 1) // items_por_pagina
    
    # Empezar en la primera página
    pagina_actual = 1

    # Bucle infinito que se rompe cuando el usuario decide salir
    while True:
        try:
            inicio = (pagina_actual - 1) * items_por_pagina
            fin = min(inicio + items_por_pagina, total_items)
            items_pagina = resultados[inicio:fin]
            
            print('\n' + '=' * 70)
            print(f'{titulo}')
            
            # Mostrar información de paginación
            # Ejemplo: 'Página 2 de 3 | Mostrando 11-20 de 25 resultados'
            # Nota: inicio + 1 porque los índices empiezan en 0 pero queremos mostrar desde 1
            print(f'Página {pagina_actual} de {total_paginas} | Mostrando {inicio + 1}-{fin} de {total_items} resultados')
            print('=' * 70)
            
            for i, item in enumerate(items_pagina, start=inicio + 1):
                # Usar la función formatear_pais() para dar formato a cada item
                print(formatear_pais(item, i, tipo_formato))

            print('\n' + '-' * 70)
            
            # Lista para almacenar los controles disponibles en esta página
            controles = []
            
            # Solo mostrar 'Siguiente' si NO estamos en la última página
            if pagina_actual < total_paginas:
                controles.append('Enter = Siguiente')
            
            # Solo mostrar 'Anterior' si NO estamos en la primera página
            if pagina_actual > 1:
                controles.append('A = Anterior')
            
            # Estos controles están disponibles siempre
            controles.append('[Número] = Ir a página')
            controles.append('S = Salir')
            
            # Unir todos los controles con ' | ' como separador
            # Ejemplo: 'Enter = Siguiente | A = Anterior | S = Salir'
            print(' | '.join(controles))
            print('-' * 70 )

            opcion = input('\nSeleccione una opción: ').lower().strip()

            if opcion == 's':
                break

            elif opcion == 'a' and pagina_actual > 1:
                pagina_actual -= 1
            
            elif opcion == 'a' and pagina_actual == 1:
                print('Ya estás en la primera página.')
                input('Presione Enter para continuar...')
    
            elif opcion == '' and pagina_actual < total_paginas:
                pagina_actual += 1
            
            elif opcion == '' and pagina_actual >= total_paginas:
                print('Ya estás en la última página.')
                input('Presione Enter para continuar...')

            elif opcion.isdigit():
                pagina_destino = int(opcion)

                if 1 <= pagina_destino <= total_paginas:
                    pagina_actual = pagina_destino
                else:
                    print(f'\nPágina inválida. Debe estar entre 1 y {total_paginas}.')
                    input('Presione Enter para continuar...')
            else:
                print(f'\nOpción "{opcion}" no reconocida.')
                print('Use: Enter (siguiente), A (anterior), [número] (ir a página), S (salir)')
                input('Presione Enter para continuar...')

        except KeyboardInterrupt:
            print('\n\n==== Paginación interrumpida por el usuario (Ctrl+C) ====')
            break  # Salir del bucle
        
        # Capturar cualquier otro error inesperado
        except Exception as e:
            print(f'\n==== Error inesperado en el paginador: {e} ====')
            break  # Salir del bucle