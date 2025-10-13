from .filtros import filtrar_por_continente, filtrar_por_rango, buscar_pais
from .ordenar import ordenar_paises
from .estadistica import mostrar_estadisticas
from .paginador import mostrar_con_paginacion

'''
Módulo con las funciones que manejan cada opción del menú principal.
'''

def opcion_buscar_pais(paises):
    # Opción 1: Buscar país por nombre
    try:
        nombre = input('Ingrese el nombre del país: ')
        
        if not nombre.strip():
            raise ValueError('El nombre no puede estar vacío')
        
        resultados = buscar_pais(paises, nombre)
        
        if resultados:
            # Usar paginador con formato simple
            mostrar_con_paginacion(resultados, titulo=f'Países que coinciden con "{nombre}"')
        else:
            print('No se encontraron coincidencias.')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


def opcion_filtrar_continente(paises):
    # Opción 2: Filtrar países por continente
    try:
        continente = input('Ingrese el continente: ')
        
        if not continente.strip():
            raise ValueError('El continente no puede estar vacío')
        
        resultados = filtrar_por_continente(paises, continente)
        
        if resultados:
            # Usar paginador con formato simple
            mostrar_con_paginacion(
                resultados,
                titulo=f'Países en {continente}'
            )
        else:
            print(f'No hay países en el continente "{continente}".')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


def opcion_filtrar_poblacion(paises):
    # Opción 3: Filtrar países por rango de población
    try:
        minimo_str = input('Ingrese población mínima: ')
        maximo_str = input('Ingrese población máxima: ')
        
        if not minimo_str.strip() or not maximo_str.strip():
            raise ValueError('Los valores no pueden estar vacíos')
        
        if not minimo_str.isdigit() or not maximo_str.isdigit():
            raise ValueError('Debe ingresar números enteros positivos')
        
        minimo = int(minimo_str)
        maximo = int(maximo_str)
        
        if minimo < 0 or maximo < 0:
            raise ValueError('Los valores deben ser positivos')
        
        if minimo > maximo:
            raise ValueError('El valor mínimo no puede ser mayor que el máximo')
        
        resultados = filtrar_por_rango(paises, 'poblacion', minimo, maximo)
        
        if resultados:
            # Usar paginador con formato de población
            mostrar_con_paginacion(
                resultados,
                titulo=f'Países con población entre {minimo:,} y {maximo:,}',
                tipo_formato='poblacion'
            )
        else:
            print('No se encontraron países en ese rango de población.')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


def opcion_filtrar_superficie(paises):
    # Opción 4: Filtrar países por rango de superficie
    try:
        minimo_str = input('Ingrese superficie mínima (km²): ')
        maximo_str = input('Ingrese superficie máxima (km²): ')
        
        if not minimo_str.strip() or not maximo_str.strip():
            raise ValueError('Los valores no pueden estar vacíos')
        
        if not minimo_str.isdigit() or not maximo_str.isdigit():
            raise ValueError('Debe ingresar números enteros positivos')
        
        minimo = int(minimo_str)
        maximo = int(maximo_str)
        
        if minimo < 0 or maximo < 0:
            raise ValueError('Los valores deben ser positivos')
        
        if minimo > maximo:
            raise ValueError('El valor mínimo no puede ser mayor que el máximo')
        
        resultados = filtrar_por_rango(paises, 'superficie', minimo, maximo)
        
        if resultados:
            # Usar paginador con formato de superficie
            mostrar_con_paginacion(
                resultados,
                titulo=f'Países con superficie entre {minimo:,} y {maximo:,} km²',
                tipo_formato='superficie'
            )
        else:
            print('No se encontraron países en ese rango de superficie.')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


def opcion_ordenar_paises(paises):
    # Opción 5: Ordenar países por diferentes criterios
    try:
        print('\nOpciones de ordenamiento:')
        print('  - nombre')
        print('  - poblacion')
        print('  - superficie')
        
        clave = input('Ordenar por: ').lower().strip()
        
        if not clave:
            raise ValueError('Debe ingresar una opción de ordenamiento')
        
        claves_validas = ['nombre', 'poblacion', 'superficie']
        if clave not in claves_validas:
            raise ValueError(f'Opción inválida. Use: {', '.join(claves_validas)}')
        
        desc_input = input('¿Descendente? (s/n): ').lower().strip()
        
        if desc_input not in ['s', 'n']:
            raise ValueError('Debe ingresar "s" para sí o "n" para no')
        
        desc = desc_input == 's'
        
        resultados = ordenar_paises(paises, clave, desc)
        
        if resultados:
            orden = 'descendente' if desc else 'ascendente'
            
            # Seleccionar tipo de formato según la clave
            if clave == 'poblacion':
                tipo = 'poblacion'
            elif clave == 'superficie':
                tipo = 'superficie'
            else:
                tipo = 'simple'
            
            # Usar paginador
            mostrar_con_paginacion(
                resultados,
                titulo=f'Países ordenados por {clave} ({orden})',
                tipo_formato=tipo
            )
        else:
            print('\nNo hay países para ordenar.')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')


def opcion_mostrar_estadisticas(paises):
    # Opción 6: Mostrar estadísticas generales
    try:
        mostrar_estadisticas(paises)
    except Exception as e:
        print(f'Error al mostrar estadísticas: {e}')