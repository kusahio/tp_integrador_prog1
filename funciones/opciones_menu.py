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
    # Opción 1: Búsqueda parcial por nombre con interacción en bucle
    while True:
        try:
            # Pide el nombre a buscar y quita espacios al inicio/fin
            nombre = input('Ingrese el nombre del país: ').strip()
            
            # Valida que no esté vacío
            if not nombre:
                raise ValueError('El nombre no puede estar vacío')
            # Valida que no contenga dígitos
            elif any(caracter.isdigit() for caracter in nombre):
                raise TypeError('El nombre no puede contener números')
            
            # Busca países que coincidan parcialmente con el nombre ingresado
            resultados = buscar_pais(paises, nombre)
            
            # Muestra resultados con paginación si hay coincidencias
            if resultados:
                mostrar_con_paginacion(resultados, titulo=f'Países que coinciden con {nombre}')
            else:
                # Informa si no se hallaron coincidencias
                print('No se encontraron coincidencias.')
        
        # Maneja errores de validación y vuelve a pedir el nombre
        except (ValueError, TypeError) as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        # Pregunta si se desea realizar otra búsqueda; si no, sale del bucle
        if not preguntar_si_no('\n¿Buscar otro país? (s/n): '):
            break


def opcion_filtrar_continente(paises):
    # Opción 2: Filtrar países por continente
    while True:
        try:
            # Solicita el nombre del continente y elimina espacios extra
            continente = input('Ingrese el continente: ').strip()
            
            # Valida que no esté vacío
            if not continente:
                raise ValueError('El continente no puede estar vacío')
            # Valida que no contenga números
            elif any(caracter.isdigit() for caracter in continente):
                raise TypeError('El continente no puede contener números')
            
            # Filtra los países que pertenecen al continente ingresado
            resultados = filtrar_por_continente(paises, continente)
            
            # Si hay resultados, los muestra con paginación
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países en {continente.title()}'
                )
            else:
                # Informa si no se encontraron países en ese continente
                print(f'No hay países en el continente {continente}.')
        
        # Captura cualquier error y permite reintentar
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        # Pregunta si se desea realizar otro filtrado; si no, sale del bucle
        if not preguntar_si_no('\n¿Filtrar otro continente? (s/n): '):
            break


def opcion_filtrar_poblacion(paises):
    # Opción 3: filtrar países por un rango de población
    while True:
        try:
            try:
                # Solicita valores mínimos y máximos y los convierte a enteros
                minimo = int(input('Ingrese población mínima: ').strip())
                maximo = int(input('Ingrese población máxima: ').strip())
            except ValueError:
                # Si la conversión falla, informa que deben ser enteros
                raise ValueError('Debe ingresar solo números enteros positivos')
            
            # Valida que ambos valores sean no negativos
            if minimo < 0 or maximo < 0:
                raise ValueError('Los valores deben ser positivos')
            # Valida que el mínimo no sea mayor que el máximo
            if minimo > maximo:
                raise ValueError('El mínimo no puede ser mayor que el máximo')

            # Filtra los países cuyo campo 'poblacion' esté dentro del rango [minimo, maximo]
            resultados = filtrar_por_rango(paises, 'poblacion', minimo, maximo)

            # Si hay resultados, los muestra con paginación y formato de población
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países con población entre {minimo:,} y {maximo:,}',
                    tipo_formato='poblacion'
                )
            else:
                # Mensaje cuando no se encuentran coincidencias en el rango dado
                print('No se encontraron países en ese rango de población.')

        # Captura cualquier error y permite reintentar sin salir del bucle
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.\n')
            continue

        # Pregunta si se desea realizar otro filtrado; si no, sale del bucle
        if not preguntar_si_no('\n¿Filtrar otro rango de población? (s/n): '):
            break


def opcion_filtrar_superficie(paises):
    # Opción 4: Filtrar países por rango de superficie
    while True:
        try:
            # Intenta leer los límites del rango como enteros
            try:
                minimo = int(input('Ingrese superficie mínima (km²): ').strip())
                maximo = int(input('Ingrese superficie máxima (km²): ').strip())
            except ValueError:
                # Si la conversión a int falla, se informa con un mensaje claro
                raise ValueError('Debe ingresar solo números enteros positivos')
            
            # Validaciones de negocio para el rango ingresado
            if minimo < 0 or maximo < 0:
                raise ValueError('Los valores deben ser positivos')
            if minimo > maximo:
                raise ValueError('El mínimo no puede ser mayor que el máximo')

            # Aplica el filtro por rango usando el campo 'superficie'
            resultados = filtrar_por_rango(paises, 'superficie', minimo, maximo)

            # Si hay resultados, los muestra con paginación y formato de superficie
            if resultados:
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países con superficie entre {minimo:,} y {maximo:,} km²',
                    tipo_formato='superficie'
                )
            else:
                # Mensaje cuando no hay países en el rango solicitado
                print('No se encontraron países en ese rango de superficie.')

        # Cualquier excepción se captura, muestra aviso y reinicia el ciclo
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.')
            continue

        # Consulta al usuario si desea realizar otro filtrado
        if not preguntar_si_no('\n¿Filtrar otro rango de superficie? (s/n): '):
            break


def opcion_ordenar_paises(paises):
    # Opción 5: Ordenar países por diferentes criterios
    while True:
        try:
            # Muestra las opciones disponibles de campos para ordenar
            print('\nOpciones de ordenamiento:')
            print('  - nombre')
            print('  - poblacion')
            print('  - superficie\n')
            
            # Toma la clave de ordenamiento y la normaliza
            clave = input('Ordenar por: ').lower().strip()
            
            # Valida que el usuario haya ingresado algo
            if not clave:
                raise ValueError('Debe ingresar una opción de ordenamiento')
            
            # Define las claves válidas y verifica la entrada
            claves_validas = ['nombre', 'poblacion', 'superficie']
            if clave not in claves_validas:
                # Nota: uso comillas dobles en el f-string para evitar conflicto con las simples internas
                raise ValueError(f"Opción inválida. Use: {', '.join(claves_validas)}")
            
            # Pregunta si el orden debe ser descendente (True/False)
            desc = preguntar_si_no('¿Descendente? (s/n): ')
            
            # Ordena la lista según la clave y el sentido elegido
            resultados = ordenar_paises(paises, clave, desc)
            
            if resultados:
                # Determina el texto del orden para el título
                orden = 'descendente' if desc else 'ascendente'
                
                # Selecciona el tipo de formato para la visualización según la clave
                if clave == 'poblacion':
                    tipo = 'poblacion'
                elif clave == 'superficie':
                    tipo = 'superficie'
                else:
                    tipo = 'simple'
                
                # Usa el paginador para mostrar los resultados ordenados
                mostrar_con_paginacion(
                    resultados,
                    titulo=f'Países ordenados por {clave} ({orden})',
                    tipo_formato=tipo
                )
            else:
                # Si no hay países cargados o la lista quedó vacía
                print('\nNo hay países para ordenar.')
        
        # Captura cualquier excepción, avisa y reinicia el ciclo
        except Exception as e:
            print(f'\nAVISO: {e}. Intente nuevamente.')
            continue

        # Consulta si se desea realizar otro ordenamiento; si no, sale del bucle
        if not preguntar_si_no('\n¿Ordenar de otra manera? (s/n): '):
            break

def opcion_mostrar_estadisticas(paises):
    # Opción 6: Mostrar estadísticas generales
    try:
        # Llama a la función que calcula y muestra estadísticas sobre la lista de países
        mostrar_estadisticas(paises)
    except Exception as e:
        # Captura cualquier error inesperado y muestra un mensaje al usuario
        print(f'Error al mostrar estadísticas: {e}')


def opcion_agregar_pais(paises, ruta_archivo):
    # Opción 7: Agregar país
    while True:
        try:
            # Encabezado de la operación
            print('\n==== Agregar nuevo país ====\n')

            # Solicita y normaliza el nombre (minúsculas para comparar; luego se formatea con title() al guardar)
            nombre = input('Ingrese nombre del país: ').strip().lower()
            
            # Validación: nombre no vacío
            if not nombre:
                raise ValueError('El nombre no puede estar vacío')
            # Validación: el nombre no debe contener números
            if any(caracter.isdigit() for caracter in nombre):
                raise TypeError('El nombre no puede contener números')

            # Validación: evitar duplicados usando comparación sin tildes y en minúsculas
            if any(quitar_tildes(pais['nombre'].lower()) == quitar_tildes(nombre) for pais in paises):
                raise ValueError(f'El país "{nombre.capitalize()}" ya existe!')

            # --- POBLACIÓN ---
            try:
                # Lee y convierte la población a entero
                poblacion = int(input('Ingrese la población del país: ').strip())
                # Validación: debe ser > 0
                if poblacion <= 0:
                    raise ValueError('La población debe ser mayor a 0')
            except ValueError as e:
                # Mensaje más claro cuando falla la conversión de string a int
                if 'invalid literal' in str(e):
                    raise ValueError('La población debe ser un número entero')
                # Re-lanza si el error fue por otra causa (p.ej., <= 0)
                raise
            
            # --- SUPERFICIE ---
            try:
                # Lee y convierte la superficie a entero
                superficie = int(input('Ingrese la superficie del país (km²): ').strip())
                # Validación: debe ser > 0
                if superficie <= 0:
                    raise ValueError('La superficie debe ser mayor a 0')
            except ValueError as e:
                # Mensaje más claro cuando falla la conversión de string a int
                if 'invalid literal' in str(e):
                    raise ValueError('La superficie debe ser un número entero')
                # Re-lanza si el error fue por otra causa (p.ej., <= 0)
                raise

            # --- CONTINENTE ---
            continentes = ['África', 'América del Norte', 'América del Sur', 'Asia', 'Europa', 'Oceanía']
            print('\nContinentes disponibles:')
            for i, continente in enumerate(continentes):
                print(f'  {i+1}) {continente}')
            
            # Lee la opción de continente como texto
            opcion = input('\nIngresa el número de opción del continente del país: ').strip()
            
            # Validación: no vacío
            if not opcion:
                raise ValueError('La opción no puede estar vacía')
            # Validación: debe ser numérica
            if not opcion.isdigit():
                raise ValueError('Debes ingresar un número de opción válido')
            
            # Convierte a índice basado en 0
            indice = int(opcion) - 1
            # Validación: índice dentro del rango de la lista
            if indice > len(continentes) - 1:
                raise IndexError('La opción está fuera de rango')
            # Validación redundante (coherencia con la lista de continentes)
            if continentes[indice] not in continentes:
                raise ValueError(f'El continente debe ser uno de: {", ".join(opcion.capitalize() for opcion in continentes)}')
            
            # --- RESUMEN ---
            print('\n' + '-'*50)
            print('Resumen del país que vas a agregar:')
            print('-'*50)
            print(f'  Nombre      : {nombre.title()}')
            print(f'  Población   : {poblacion:,} habitantes')
            print(f'  Superficie  : {superficie:,} km²')
            print(f'  Continente  : {continentes[indice]}')
            print('-'*50 + '\n')
            
            # Confirmación antes de persistir
            if not preguntar_si_no('¿Confirma que desea agregar este país? (s/n): '):
                print('\nOperación cancelada.')
                break

            # Arma el diccionario con el formato final
            nuevo_pais = {
                'nombre': nombre.title(),
                'poblacion': poblacion,
                'superficie': superficie,
                'continente': continentes[indice]
            }
            
            # Intenta agregar el país (persiste y luego agrega en memoria)
            if agregar_pais(paises, nuevo_pais, ruta_archivo):
                print('\n✓ ¡País agregado exitosamente!')
                print(f'  Total de países: {len(paises)}')
            else:
                print('\nNo se pudo agregar el país.')

        # Manejo de errores esperados: validaciones de entrada y rango
        except (ValueError, TypeError, IndexError) as e:
            print(f'\nAVISO: {e}')
            # Ofrece volver a intentar; si no, sale del bucle
            if not preguntar_si_no('\n¿Desea intentar nuevamente? (s/n): '):
                break
            continue
        
        # Permite cancelar con Ctrl+C de forma limpia
        except KeyboardInterrupt:
            print('\n\nOperación cancelada por el usuario.')
            break
        
        # Cualquier otro error no contemplado
        except Exception as e:
            print(f'\nError inesperado: {e}')
            break
        
        # Pregunta si se desea agregar otro país; si no, termina
        if not preguntar_si_no('\n¿Desea agregar otro país? (s/n): '):
            break


def opcion_editar_pais(paises, ruta_archivo):
    # Opción 8: Editar país
    while True:
        try:
            # Encabezado visual de la sección
            print('\n==== Editar País ====\n')
            
            # Busca un país por nombre y obtiene su índice en la lista
            pais_encontrado, indice_pais = buscar_y_seleccionar_pais(paises)

            # Si no se encontró o el usuario canceló, ofrecer reintentar
            if pais_encontrado is None:
                if not preguntar_si_no('\n¿Desea intentar con otro nombre? (s/n): '):
                    break
                continue

            # Menú de campos a editar
            print('\n¿Qué campos deseas editar?\n')
            print('  1) Nombre\n  2) Población\n  3) Superficie\n  4) Continente\n  5) Todo\n  6) Cancelar')
            
            # Lee la opción del usuario y valida que sea numérica
            try:
                opcion_editar = int(input('\nOpción: ').strip())
            except ValueError:
                print('\nDebe ingresar un número válido.')
                continue

            # Procesar la opción elegida usando pattern matching
            match opcion_editar:
                case 1:
                    # Editar solo el nombre
                    nuevo_nombre = solicitar_nuevo_nombre(paises, pais_encontrado)
                    if editar_campo_pais(paises, indice_pais, 'nombre', nuevo_nombre, ruta_archivo):
                        print('\nNombre actualizado correctamente.')
                case 2:
                    # Editar solo la población (con confirmación)
                    nueva_poblacion = solicitar_valor_numerico('\nNueva población: ')
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'poblacion', nueva_poblacion, ruta_archivo):
                            print('\nPoblación actualizada correctamente.')
                case 3:
                    # Editar solo la superficie (con confirmación)
                    nueva_superficie = solicitar_valor_numerico('\nNueva superficie (km²): ')
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'superficie', nueva_superficie, ruta_archivo):
                            print('\nSuperficie actualizada correctamente.')
                case 4:
                    # Editar solo el continente (con confirmación)
                    nuevo_continente = solicitar_nuevo_continente()
                    if preguntar_si_no('¿Confirma el cambio? (s/n):'):
                        if editar_campo_pais(paises, indice_pais, 'continente', nuevo_continente, ruta_archivo):
                            print('\nContinente actualizado correctamente.')
                case 5:
                    # Editar todos los campos con un resumen de cambios previo
                    print('\n==== Ingrese los Nuevos Datos ====')
                    nuevo_nombre = solicitar_nuevo_nombre(paises, pais_encontrado)
                    nueva_poblacion = solicitar_valor_numerico('Nueva población: ')
                    nueva_superficie = solicitar_valor_numerico('Nueva superficie (km²): ')
                    nuevo_continente = solicitar_nuevo_continente()
                    
                    # Mostrar un resumen de lo que se va a modificar
                    print('\nResumen de cambios:')
                    print('-'*70)
                    print(f'  Nombre      : {pais_encontrado["nombre"]} --> {nuevo_nombre}')
                    print(f'  Población   : {pais_encontrado["poblacion"]:,} --> {nueva_poblacion:,}')
                    print(f'  Superficie  : {pais_encontrado["superficie"]:,} --> {nueva_superficie:,} km²')
                    print(f'  Continente  : {pais_encontrado["continente"]} --> {nuevo_continente}')
                    
                    # Confirmación final antes de persistir todos los cambios
                    if preguntar_si_no('\n¿Confirma los cambios? (s/n): '):
                        # Actualiza en memoria el país con los nuevos datos
                        paises[indice_pais].update({
                            'nombre': nuevo_nombre,
                            'poblacion': nueva_poblacion,
                            'superficie': nueva_superficie,
                            'continente': nuevo_continente
                        })
                        # Intenta guardar toda la lista en el archivo
                        if guardar_paises(ruta_archivo, paises):
                            print('\n¡País actualizado correctamente!')
                        else:
                            print('\nNo se pudieron guardar los cambios.')
                    else:
                        print('\nCambios cancelados.')

                case 6:
                    # Cancela la edición y vuelve al menú anterior
                    print('\nOperación cancelada.')
                case _:
                    # Opción fuera del rango permitido
                    print('\nOpción inválida. Debe elegir entre 1 y 6.')

            # Si canceló (opción 6) o no desea seguir editando, salir del bucle
            if opcion_editar == 6 or not preguntar_si_no('\n¿Desea editar otro país? (s/n): '):
                break

        # Permite al usuario abortar con Ctrl+C de forma limpia
        except KeyboardInterrupt:
            print('\n\nOperación cancelada por el usuario.')
            break
        # Captura cualquier otro error inesperado y termina la operación
        except Exception as e:
            print(f'\nError inesperado: {e}')
            break

def opcion_eliminar_pais(paises, ruta_archivo):
    # Opción 9: Eliminar país
    while True:
        try:
            # Muestra encabezado de la acción
            print('\n==== Eliminar País ====\n')

            # Busca y confirma el país a eliminar (retorna el dict y su índice)
            pais_encontrado, indice_pais = buscar_y_seleccionar_pais(paises, 'eliminar')

            # Si no se encontró o el usuario canceló, ofrece intentar nuevamente
            if pais_encontrado is None:
                if not preguntar_si_no('\n¿Deseas intentar con otro nombre? (s/n): '):
                    break
                continue

            # Advierte al usuario sobre la eliminación permanente
            print(f'\nAVISO: Estás a punto de eliminar a "{pais_encontrado["nombre"]}" de forma permanente.')

            # Confirma por segunda vez antes de proceder
            if preguntar_si_no('¿Estás realmente seguro de que deseas continuar? (s/n): '):
                # Quita el país de la lista en memoria (operación temporal)
                pais_a_eliminar = paises.pop(indice_pais)

                # Intenta persistir el cambio en el archivo CSV
                if guardar_paises(ruta_archivo, paises):
                    # Confirmación de eliminación exitosa
                    print(f'\nEl país "{pais_a_eliminar["nombre"]}" ha sido eliminado exitosamente.')
                    print(f'Total de países restantes: {len(paises)}')
                else:
                    # Si falla el guardado, revierte la eliminación en memoria
                    paises.insert(indice_pais, pais_a_eliminar)
                    print('\nAVISO: No se pudieron guardar los cambios. La eliminación ha sido revertida.')
            else:
                # El usuario canceló en la segunda confirmación
                print('\nOperación de eliminación cancelada.')

            # Pregunta si se desea eliminar otro país
            if not preguntar_si_no('\n¿Desea eliminar otro país? (s/n): '):
                break

        # Permite salir con Ctrl+C informando la cancelación
        except KeyboardInterrupt:
            print('\nOperación cancelada por el usuario.')
            break
        # Maneja cualquier otro error inesperado
        except Exception as e:
            print(f'\nAVISO: {e}')
            break