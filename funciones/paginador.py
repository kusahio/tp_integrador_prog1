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
    try:
        # Formato con población
        if tipo_formato == 'poblacion':
            return f'  {index}. {pais["nombre"]}: {pais["poblacion"]:,} habitantes'
        
        # Formato con superficie
        elif tipo_formato == 'superficie':
            return f'  {index}. {pais["nombre"]}: {pais["superficie"]:,} km²'
        
        # Formato completo con toda la información
        elif tipo_formato == 'completo':
            return (f'  {index}. {pais["nombre"]}\n'
                    f'      Continente: {pais["continente"]}\n'
                    f'      Población: {pais["poblacion"]:,} habitantes\n'
                    f'      Superficie: {pais["superficie"]:,} km²')
        
        # Formato simple (por defecto)
        else:
            return f'  {index}. {pais["nombre"]} - {pais["continente"]}'
    
    except KeyError as e:
        return f'  {index}. Error: Falta el campo {e}'
    except (TypeError, ValueError) as e:
        return f'  {index}. Error de formato: {e}'


def mostrar_pagina(items, inicio_idx, titulo_pagina, tipo_formato='simple'):
    '''
    Función auxiliar para mostrar una página de resultados.
    
    Args:
        items (list): Lista de items a mostrar
        inicio_idx (int): Índice inicial para la numeración
        titulo_pagina (str): Título a mostrar en el encabezado
        tipo_formato (str): Tipo de formato para formatear_pais
    '''
    print('\n' + '=' * 77)
    print(f'{titulo_pagina}')
    print('=' * 77, '\n')
    
    for i, item in enumerate(items, start=inicio_idx):
        print(formatear_pais(item, i, tipo_formato))
    
    print('\n' + '-' * 77)


def mostrar_con_paginacion(resultados, items_por_pagina=10, titulo='Resultados', tipo_formato='simple'):
    '''
    Muestra resultados con paginación adaptativa según la cantidad de resultados.
    
    Comportamiento:
    - ≤10 resultados (1 página): Solo muestra resultados, Enter para continuar
    - 2 páginas: Enter (siguiente), A (anterior), S (salir)
    - >2 páginas: Enter (siguiente), A (anterior), [Número] (ir a página), S (salir)
    - En última página: Enter vuelve a página 1
    
    Ejemplo de uso:
        mostrar_con_paginacion(paises, titulo='Países encontrados')
        mostrar_con_paginacion(paises, tipo_formato='poblacion')
    '''
    try:
        # Verificar si hay resultados para mostrar
        if not resultados:
            print('\nNo hay resultados para mostrar.')
            return
        
        # Validar que items_por_pagina sea un número positivo
        if not isinstance(items_por_pagina, int) or items_por_pagina <= 0:
            items_por_pagina = 10

        # Contar cuántos items hay en total
        total_items = len(resultados)

        # Calcular total de páginas
        total_paginas = (total_items + items_por_pagina - 1) // items_por_pagina
        
        # Si hay 10 o menos resultados (1 sola página), mostrar y salir
        if total_items <= 10:
            titulo_completo = f'{titulo}\nMostrando {total_items} resultado{"s" if total_items != 1 else ""}'
            mostrar_pagina(resultados, 1, titulo_completo, tipo_formato)
            input('Presione Enter para continuar...')
            return
        
        # Para más de 10 resultados, usar paginación completa
        pagina_actual = 1

        while True:
            inicio = (pagina_actual - 1) * items_por_pagina
            fin = min(inicio + items_por_pagina, total_items)
            items_pagina = resultados[inicio:fin]
            
            # Mostrar página actual
            titulo_pagina = f'{titulo}\nPágina {pagina_actual} de {total_paginas} | Mostrando {inicio + 1}-{fin} de {total_items} resultados'
            mostrar_pagina(items_pagina, inicio + 1, titulo_pagina, tipo_formato)
            
            # Construir controles según el contexto
            controles = []
            
            # Enter siempre disponible
            if pagina_actual < total_paginas:
                controles.append('Enter = Siguiente')
            else:
                controles.append('Enter = Volver a página 1')
            
            # A (Anterior) disponible si hay más de 1 página y no estamos en la primera
            if total_paginas >= 2 and pagina_actual > 1:
                controles.append('A = Anterior')
            
            # [Número] solo disponible si hay más de 2 páginas
            if total_paginas > 2:
                controles.append('[Número] = Ir a página')
            
            # S (Salir) disponible si hay más de 1 página
            if total_paginas >= 2:
                controles.append('S = Salir')
            
            print(' | '.join(controles))
            print('-' * 77)

            opcion = input('\nSeleccione una opción: ').lower().strip()

            # Opción salir (disponible con 2 o más páginas)
            if opcion == 's' and total_paginas >= 2:
                break

            # Página anterior (disponible con 2 o más páginas)
            elif opcion == 'a' and pagina_actual > 1:
                pagina_actual -= 1
            
            elif opcion == 'a' and pagina_actual == 1:
                print('\nYa estás en la primera página.')
                input('Presione Enter para continuar...')
    
            # Enter: siguiente o volver a página 1
            elif opcion == '':
                if pagina_actual < total_paginas:
                    pagina_actual += 1
                else:
                    # En última página, volver a página 1
                    pagina_actual = 1

            # Ir a página específica (solo con más de 2 páginas)
            elif opcion.isdigit() and total_paginas > 2:
                pagina_destino = int(opcion)
                if 1 <= pagina_destino <= total_paginas:
                    pagina_actual = pagina_destino
                else:
                    print(f'\nPágina inválida. Debe estar entre 1 y {total_paginas}.')
                    input('Presione Enter para continuar...')
            
            # Opción no reconocida
            else:
                print(f'\nOpción "{opcion}" no reconocida.')
                opciones_validas = ['Enter']
                if total_paginas >= 2 and pagina_actual > 1:
                    opciones_validas.append('A (anterior)')
                if total_paginas > 2:
                    opciones_validas.append('[número] (ir a página)')
                if total_paginas >= 2:
                    opciones_validas.append('S (salir)')
                print(f'Opciones válidas: {", ".join(opciones_validas)}')
                input('Presione Enter para continuar...')

    except KeyboardInterrupt:
        print('\n\nAVISO: Paginación interrumpida por el usuario')
    except Exception as e:
        print(f'\nAVISO: Error inesperado en el paginador - {e}')