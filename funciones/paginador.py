
def formatear_pais(pais, index, tipo_formato='simple'):
    '''
    Args:
        pais (dict): Diccionario con información del país
        index (int): Número de índice a mostrar
        tipo_formato (str): Tipo de formato: 'simple', 'poblacion', 'superficie', 'completo'
    Ejemplos:
        formatear_pais({'nombre': 'Argentina', 'continente': 'América'}, 1, 'simple')
        → ' 1. Argentina - América'
        formatear_pais({'nombre': 'Argentina', 'poblacion': 45000000}, 1, 'poblacion')
        → ' 1. Argentina: 45,000,000 habitantes'
    '''
    try:
        # Formato con población: muestra nombre y población con separador de miles
        if tipo_formato == 'poblacion':
            return f' {index}. {pais["nombre"]}: {pais["poblacion"]:,} habitantes'

        # Formato con superficie: muestra nombre y superficie con separador de miles
        elif tipo_formato == 'superficie':
            return f' {index}. {pais["nombre"]}: {pais["superficie"]:,} km²'

        # Formato completo: incluye continente, población y superficie en varias líneas
        elif tipo_formato == 'completo':
            return (f' {index}. {pais["nombre"]}\n'
                    f'   Continente: {pais["continente"]}\n'
                    f'   Población : {pais["poblacion"]:,} habitantes\n'
                    f'   Superficie: {pais["superficie"]:,} km²')

        # Formato simple (por defecto): nombre - continente en una línea
        else:
            return f' {index}. {pais["nombre"]} - {pais["continente"]}'

    # Si falta alguna clave esperada en el diccionario 'pais'
    except KeyError as e:
        return f' {index}. Error: Falta el campo {e}'

    # Si se reciben tipos erróneos o hay problemas de formato
    except (TypeError, ValueError) as e:
        return f' {index}. Error de formato: {e}'


def mostrar_pagina(items, inicio_idx, titulo_pagina, tipo_formato='simple'):
    '''
    Función auxiliar para mostrar una página de resultados.
    Args:
        items (list): Lista de items (países) a mostrar
        inicio_idx (int): Índice inicial para la numeración visual
        titulo_pagina (str): Título a mostrar en el encabezado
        tipo_formato (str): Tipo de formato a usar en formatear_pais
    '''
    # Encabezado visual de la página
    print('\n' + '=' * 80)
    print(f'{titulo_pagina}')
    print('=' * 80, '\n')

    # Recorre y muestra cada item usando el formateador elegido
    for i, item in enumerate(items, start=inicio_idx):
        print(formatear_pais(item, i, tipo_formato))

    # Separador inferior
    print('\n' + '-' * 80)


def mostrar_con_paginacion(resultados, items_por_pagina=10, titulo='Resultados', tipo_formato='simple'):
    try:
        # Verificar si hay resultados para mostrar
        if not resultados:
            print('\nNo hay resultados para mostrar.')
            return

        # Validar que items_por_pagina sea un entero positivo; si no, usar 10 por defecto
        if not isinstance(items_por_pagina, int) or items_por_pagina <= 0:
            items_por_pagina = 10

        # Total de elementos y cálculo de páginas (redondeo hacia arriba)
        total_items = len(resultados)
        total_paginas = (total_items + items_por_pagina - 1) // items_por_pagina

        # Caso simple: 10 o menos resultados → una sola pantalla y volver
        if total_items <= 10:
            titulo_completo = f'{titulo}\nMostrando {total_items} resultado{"s" if total_items != 1 else ""}'
            mostrar_pagina(resultados, 1, titulo_completo, tipo_formato)
            input('Presione Enter para continuar...')
            return

        # Paginación interactiva para más de 10 resultados
        pagina_actual = 1
        while True:
            # Determina el rango (slice) de la página actual
            inicio = (pagina_actual - 1) * items_por_pagina
            fin = min(inicio + items_por_pagina, total_items)
            items_pagina = resultados[inicio:fin]

            # Muestra la página actual con título informativo
            titulo_pagina = (
                f'{titulo}\n'
                f'Página {pagina_actual} de {total_paginas} \n'
                f'  Mostrando {inicio + 1}-{fin} de {total_items} resultados'
            )
            mostrar_pagina(items_pagina, inicio + 1, titulo_pagina, tipo_formato)

            # Construcción de controles visibles según el contexto
            controles = []
            # Enter (siguiente / volver a 1 en última)
            if pagina_actual < total_paginas:
                controles.append('Enter = Siguiente')
            else:
                controles.append('Enter = Volver a página 1')
            # A (Anterior) si no estamos en la primera
            if total_paginas >= 2 and pagina_actual > 1:
                controles.append('A = Anterior')
            # [Número] para ir a una página específica (si hay más de 2 páginas)
            if total_paginas > 2:
                controles.append('[Número] = Ir a página')
            # S (Salir) disponible si hay 2 o más páginas
            if total_paginas >= 2:
                controles.append('S = Salir')

            # Muestra controles y lee la opción del usuario
            print(' | '.join(controles))
            print('-' * 80)
            opcion = input('\nSeleccione una opción: ').lower().strip()

            # Opción salir (con 2 o más páginas)
            if opcion == 's' and total_paginas >= 2:
                break

            # Ir a la página anterior (si es posible)
            elif opcion == 'a' and pagina_actual > 1:
                pagina_actual -= 1
            elif opcion == 'a' and pagina_actual == 1:
                # Ya no se puede ir más atrás
                print('\nYa estás en la primera página.')
                input('Presione Enter para continuar...')

            # Enter: avanzar; si estamos en la última, volver a la primera
            elif opcion == '':
                if pagina_actual < total_paginas:
                    pagina_actual += 1
                else:
                    pagina_actual = 1

            # Número: ir a una página específica (solo si hay > 2 páginas)
            elif opcion.isdigit() and total_paginas > 2:
                pagina_destino = int(opcion)
                if 1 <= pagina_destino <= total_paginas:
                    pagina_actual = pagina_destino
                else:
                    print(f'\nPágina inválida. Debe estar entre 1 y {total_paginas}.')
                    input('Presione Enter para continuar...')

            # Opción no reconocida: muestra ayuda contextual
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

    # Permite interrumpir con Ctrl+C de manera limpia
    except KeyboardInterrupt:
        print('\n\nAVISO: Paginación interrumpida por el usuario')

    # Cualquier otro error inesperado se informa sin romper la app
    except Exception as e:
        print(f'\nAVISO: Error inesperado en el paginador - {e}')