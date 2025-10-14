from .filtros import filtrar_por_continente, filtrar_por_rango, buscar_pais
from .ordenar import ordenar_paises
from .estadistica import mostrar_estadisticas
from .paginador import mostrar_con_paginacion

'''
Módulo con las funciones que manejan cada opción del menú principal.
'''

def preguntar_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ('s', 'n'):
            return respuesta == 's'
        print('Respuesta inválida. Ingrese "s" para sí o "n" para no.')

def opcion_buscar_pais(paises):
    while True:
        try:
            nombre = input('Ingrese el nombre del país: ').strip()
            
            if not nombre:
                raise ValueError('El nombre no puede estar vacío')
            
            resultados = buscar_pais(paises, nombre)
            
            if resultados:
                mostrar_con_paginacion(resultados, titulo=f'Países que coinciden con "{nombre}"')
            else:
                print('No se encontraron coincidencias.')
        
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        if not preguntar_si_no('\n¿Buscar otro país? (s/n): '):
            break

def opcion_filtrar_continente(paises):
    # Opción 2: Filtrar países por continente
    while True:
        try:
            continente = input('Ingrese el continente: ').strip()
            
            if not continente:
                raise ValueError('El continente no puede estar vacío')
            
            resultados = filtrar_por_continente(paises, continente)
            
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países en {continente}'
                )
            else:
                print(f'No hay países en el continente "{continente}".')
        
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        if not preguntar_si_no('\n¿Filtrar otro continente? (s/n): '):
            break

def opcion_filtrar_poblacion(paises):
    # Opción 3: filtrar por rango de población
    while True:
        try:
            try:
                minimo = int(input('Ingrese población mínima: ').strip())
                maximo = int(input('Ingrese población máxima: ').strip())
            except ValueError:
                raise ValueError('Debe ingresar solo números enteros positivos')
            
            if minimo < 0 or maximo < 0:
                raise ValueError('Los valores deben ser positivos')
            if minimo > maximo:
                raise ValueError('El mínimo no puede ser mayor que el máximo')

            resultados = filtrar_por_rango(paises, 'poblacion', minimo, maximo)
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países con población entre {minimo:,} y {maximo:,}',
                    tipo_formato='poblacion'
                )
            else:
                print('No se encontraron países en ese rango de población.')

        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        if not preguntar_si_no('\n¿Filtrar otro rango de población? (s/n): '):
            break

def opcion_filtrar_superficie(paises):
    # Opción 4: Filtrar países por rango de superficie
    while True:
        try:
            try:
                minimo = int(input('Ingrese superficie mínima (km²): ').strip())
                maximo = int(input('Ingrese superficie máxima (km²): ').strip())
            except ValueError:
                raise ValueError('Debe ingresar solo números enteros positivos')
            
            if minimo < 0 or maximo < 0:
                raise ValueError('Los valores deben ser positivos')
            if minimo > maximo:
                raise ValueError('El mínimo no puede ser mayor que el máximo')

            resultados = filtrar_por_rango(paises, 'superficie', minimo, maximo)
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países con superficie entre {minimo:,} y {maximo:,} km²',
                    tipo_formato='superficie'
                )
            else:
                print('No se encontraron países en ese rango de superficie.')

        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.')
            continue

        if not preguntar_si_no('\n¿Filtrar otro rango de superficie? (s/n): '):
            break

def opcion_ordenar_paises(paises):
    # Opción 5: Ordenar países por diferentes criterios
    while True:
        try:
            print('\nOpciones de ordenamiento:')
            print('  - nombre')
            print('  - poblacion')
            print('  - superficie\n')
            
            clave = input('Ordenar por: ').lower().strip()
            
            if not clave:
                raise ValueError('Debe ingresar una opción de ordenamiento')
            
            claves_validas = ['nombre', 'poblacion', 'superficie']
            if clave not in claves_validas:
                raise ValueError(f'Opción inválida. Use: {', '.join(claves_validas)}')
            
            desc = preguntar_si_no('¿Descendente? (s/n): ')
            
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
        
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.')
            continue

        if not preguntar_si_no('\n¿Ordenar de otra manera? (s/n): '):
            break

def opcion_mostrar_estadisticas(paises):
    # Opción 6: Mostrar estadísticas generales
    try:
        mostrar_estadisticas(paises)
    except Exception as e:
        print(f'Error al mostrar estadísticas: {e}')