from .filtros import filtrar_por_continente, filtrar_por_rango, buscar_pais
from .ordenar import ordenar_paises
from .estadistica import mostrar_estadisticas
from .paginador import mostrar_con_paginacion
from .edicion import agregar_pais, editar_campo_pais, guardar_paises
from .utilidades import preguntar_si_no,  quitar_tildes
from .auxiliares import (
    buscar_y_seleccionar_pais,
    solicitar_nuevo_continente,
    solicitar_nuevo_nombre,
    solicitar_valor_numerico
    )
'''
Módulo con las funciones que manejan cada opción del menú principal.
'''

def opcion_buscar_pais(paises):
    # Opcion 1: Búsqueda parcial con nombre
    while True:
        try:
            nombre = input('Ingrese el nombre del país: ').strip()
            
            if not nombre:
                raise ValueError('El nombre no puede estar vacío')
            elif any(caracter.isdigit() for caracter in nombre):
                raise TypeError('El nombre no puede contener números')
            
            resultados = buscar_pais(paises, nombre)
            
            if resultados:
                mostrar_con_paginacion(resultados, titulo=f'Países que coinciden con {nombre}')
            else:
                print('No se encontraron coincidencias.')
        
        except (ValueError, TypeError) as e:
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
            elif any(caracter.isdigit() for caracter in continente):
                raise TypeError('El continente no puede contener números')
            
            resultados = filtrar_por_continente(paises, continente)
            
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países en {continente.title()}'
                )
            else:
                print(f'No hay países en el continente {continente}.')
        
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

def opcion_agregar_pais(paises, ruta_archivo):
    # Opción 7: Agregar país
    while True:
        try:
            print('\n==== Agregar nuevo país ====\n')
            nombre = input('Ingrese nombre del país: ').strip().lower()
            
            if not nombre:
                raise ValueError('El nombre no puede estar vacío')
            
            if any(caracter.isdigit() for caracter in nombre):
                raise TypeError('El nombre no puede contener números')

            if any(quitar_tildes(pais['nombre'].lower()) == quitar_tildes(nombre) for pais in paises):
                raise ValueError(f'El país "{nombre.capitalize()}" ya existe!')

            try:
                poblacion = int(input('Ingrese la población del país: ').strip())
                
                if poblacion <= 0:
                    raise ValueError('La población debe ser mayor a 0')
            
            except ValueError as e:
                if 'invalid literal' in str(e):
                    raise ValueError('La población debe ser un número entero')
                raise
            
            try:
                superficie = int(input('Ingrese la superficie del país (km²): ').strip())
                
                if superficie <= 0:
                    raise ValueError('La superficie debe ser mayor a 0')
            
            except ValueError as e:
                if 'invalid literal' in str(e):
                    raise ValueError('La superficie debe ser un número entero')
                raise

            continentes = ['África', 'América del Norte', 'América del Sur', 'Asia', 'Europa', 'Oceanía']
            print('\nContinentes disponibles:')
            for i, continente in enumerate(continentes):
                print(f'  {i+1}) {continente}')
            
            opcion = input('\nIngresa el número de opción del continente del país: ').strip()
            
            if not opcion:
                raise ValueError('La opción no puede estar vacía')
            
            if not opcion.isdigit():
                raise ValueError('Debes ingresar un número de opción válido')
            
            indice = int(opcion) - 1
            if indice > len(continentes) - 1:
                raise IndexError('La opción está fuera de rango')
            if continentes[indice] not in continentes:
                raise ValueError(f'El continente debe ser uno de: {", ".join(opcion.capitalize() for opcion in continentes)}')
            
            print('\n' + '-'*50)
            print('Resumen del país que vas a agregar:')
            print('-'*50)
            print(f'  Nombre      : {nombre.title()}')
            print(f'  Población   : {poblacion:,} habitantes')
            print(f'  Superficie  : {superficie:,} km²')
            print(f'  Continente  : {continentes[indice]}')
            print('-'*50 + '\n')
            
            
            if not preguntar_si_no('¿Confirma que desea agregar este país? (s/n): '):
                print('\nOperación cancelada.')
                break

            nuevo_pais = {
                'nombre': nombre.title(),
                'poblacion': poblacion,
                'superficie': superficie,
                'continente': continentes[indice]
            }
            
            if agregar_pais(paises, nuevo_pais, ruta_archivo):
                print('\n✓ ¡País agregado exitosamente!')
                print(f'  Total de países: {len(paises)}')
            else:
                print('\nNo se pudo agregar el país.')

        except (ValueError, TypeError, IndexError) as e:
            print(f'\nAVISO: {e}')
            
            if not preguntar_si_no('\n¿Desea intentar nuevamente? (s/n): '):
                break
            continue
        
        except KeyboardInterrupt:
            print('\n\nOperación cancelada por el usuario.')
            break
        
        except Exception as e:
            print(f'\nError inesperado: {e}')
            break
        
        if not preguntar_si_no('\n¿Desea agregar otro país? (s/n): '):
            break

def opcion_editar_pais(paises, ruta_archivo):
    # Opción 8: Editar país
    while True:
        try:
            print('\n==== Editar País ====\n')
            
            pais_encontrado, indice_pais = buscar_y_seleccionar_pais(paises)

            if pais_encontrado is None:
                if not preguntar_si_no('\n¿Desea intentar con otro nombre? (s/n): '):
                    break
                continue

            print('\n¿Qué campos deseas editar?\n')
            print('  1) Nombre\n  2) Población\n  3) Superficie\n  4) Continente\n  5) Todo\n  6) Cancelar')
            
            try:
                opcion_editar = int(input('\nOpción: ').strip())
            except ValueError:
                print('\nDebe ingresar un número válido.')
                continue

            # Procesar la opción elegida
            match opcion_editar:
                case 1:
                    nuevo_nombre = solicitar_nuevo_nombre(paises, pais_encontrado)
                    if editar_campo_pais(paises, indice_pais, 'nombre', nuevo_nombre, ruta_archivo):
                        print('\nNombre actualizado correctamente.')
                case 2:
                    nueva_poblacion = solicitar_valor_numerico('\nNueva población: ')
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'poblacion', nueva_poblacion, ruta_archivo):
                            print('\nPoblación actualizada correctamente.')
                case 3:
                    nueva_superficie = solicitar_valor_numerico('\nNueva superficie (km²): ')
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'superficie', nueva_superficie, ruta_archivo):
                            print('\nSuperficie actualizada correctamente.')
                case 4:
                    nuevo_continente = solicitar_nuevo_continente()
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'continente', nuevo_continente, ruta_archivo):
                            print('\nContinente actualizado correctamente.')
                case 5:
                    print('\n==== Ingrese los Nuevos Datos ====')
                    nuevo_nombre = solicitar_nuevo_nombre(paises, pais_encontrado)
                    nueva_poblacion = solicitar_valor_numerico('Nueva población: ')
                    nueva_superficie = solicitar_valor_numerico('Nueva superficie (km²): ')
                    nuevo_continente = solicitar_nuevo_continente()
                    
                    # Mostrar resumen
                    print('\nResumen de cambios:')
                    print('-'*70)
                    print(f'  Nombre      : {pais_encontrado["nombre"]} --> {nuevo_nombre}')
                    print(f'  Población   : {pais_encontrado["poblacion"]:,} --> {nueva_poblacion:,}')
                    print(f'  Superficie  : {pais_encontrado["superficie"]:,} --> {nueva_superficie:,} km²')
                    print(f'  Continente  : {pais_encontrado["continente"]} --> {nuevo_continente}')
                    
                    if preguntar_si_no('\n¿Confirma los cambios? (s/n): '):
                        paises[indice_pais].update({
                            'nombre': nuevo_nombre,
                            'poblacion': nueva_poblacion,
                            'superficie': nueva_superficie,
                            'continente': nuevo_continente
                        })
                        if guardar_paises(ruta_archivo, paises):
                            print('\n¡País actualizado correctamente!')
                        else:
                            print('\nNo se pudieron guardar los cambios.')
                    else:
                        print('\nCambios cancelados.')

                case 6:
                    print('\nOperación cancelada.')
                case _:
                    print('\nOpción inválida. Debe elegir entre 1 y 6.')

            # Preguntar si desea editar otro país, solo si no canceló
            if opcion_editar == 6 or not preguntar_si_no('\n¿Desea editar otro país? (s/n): '):
                break

        except KeyboardInterrupt:
            print('\n\nOperación cancelada por el usuario.')
            break
        except Exception as e:
            print(f'\nError inesperado: {e}')
            break

def opcion_eliminar_pais(paises, ruta_archivo):
    # Opcion 9: Eliminar país
    while True:
        try:
            print('\n==== Eliminar País ====\n')
            pais_encontrado, indice_pais = buscar_y_seleccionar_pais(paises, 'eliminar')

            if pais_encontrado is None:
                if not preguntar_si_no('\n¿Deseas intentar con otro nombre? (s/n): '):
                    break
                continue

            print(f'\nAVISO: Estás a punto de eliminar a "{pais_encontrado["nombre"]}" de forma permanente.')

            if preguntar_si_no('¿Estás realmente seguro de que deseas continuar? (s/n): '):
                pais_a_eliminar = paises.pop(indice_pais)
                if guardar_paises(ruta_archivo, paises):
                    print(f'\nEl país "{pais_a_eliminar["nombre"]}" ha sido eliminado exitosamente.')
                    print(f'Total de países restantes: {len(paises)}')
                else:
                    paises.insert(indice_pais, pais_a_eliminar)
                    print('\nAVISO: No se pudieron guardar los cambios. La eliminación ha sido revertida.')
            
            else:
                print('\nOperación de eliminación cancelada.')

            if not preguntar_si_no('\n¿Desea eliminar otro país? (s/n): '):
                break

        except KeyboardInterrupt:
            print('\nOperación cancelada por el usuario.')
            break
        except Exception as e:
            print(f'\nAVISO: {e}')
            break