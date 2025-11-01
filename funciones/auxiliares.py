from .utilidades import preguntar_si_no, verificar_string
from .filtros import buscar_exacto

def buscar_y_seleccionar_pais(paises, accion='editar'):
    # Pide el nombre del país a buscar según la acción (editar/eliminar/etc.)
    nombre_buscar = input(f'Ingresa el nombre del país a {accion}: ').strip()
    
    # Valida que el usuario no deje el campo vacío
    if not nombre_buscar:
        print('\nEl nombre no puede estar vacío.')
        return None, None

    if not verificar_string(nombre_buscar):
        return None, None
    # Busca coincidencia exacta (según tu función buscar_exacto)
    pais_encontrado = buscar_exacto(paises, nombre_buscar)


    # Si no encuentra el país, informa y finaliza
    if pais_encontrado is None:
        print(f'\nNo se encontró ningún país con el nombre "{nombre_buscar}"')
        print('El nombre debe ser exacto (puedes omitir tildes y mayúsculas)')
        return None, None

    # Muestra un resumen del país encontrado
    print(f'\nPaís encontrado: {pais_encontrado["nombre"]}')
    print('-' * 70)
    print(f'  Población  : {pais_encontrado["poblacion"]:,} habitantes')
    print(f'  Superficie : {pais_encontrado["superficie"]:,} km²')
    print(f'  Continente : {pais_encontrado["continente"]}')
    print('-' * 70)

    # Pide confirmación para proceder con la acción
    if not preguntar_si_no(f'\n¿Es este el país que deseas {accion}? (s/n): '):
        print('\nBúsqueda cancelada.')
        return None, None
    # Obtiene el índice del país dentro de la lista original
    indice_pais = next((i for i, pais in enumerate(paises) if pais['nombre'] == pais_encontrado['nombre']), None)
    
    # Si por alguna razón no se encontró el índice, informa y finaliza
    if indice_pais is None:
        print('\AVISO: no se encontró el país en la base de datos interna.')
        return None, None

    # Devuelve el diccionario del país y su índice en la lista
    return pais_encontrado, indice_pais


def solicitar_valor_numerico(mensaje_prompt):
    # Bucle hasta que el usuario ingrese un entero positivo válido
    while True:
        try:
            # Convierte la entrada a entero después de eliminar espacios
            valor = int(input(mensaje_prompt).strip())
            # Verifica que sea mayor que cero
            if valor <= 0:
                print('El valor debe ser un número positivo.')
                continue
            # Retorna el valor válido
            return valor
        except ValueError:
            # Informa si la conversión a entero falla
            print('Debes ingresar un número entero válido.')


def solicitar_nuevo_nombre(paises, pais_actual):
    # Bucle hasta que se ingrese un nombre válido y no duplicado
    while True:
        # Pide el nuevo nombre
        nuevo_nombre = input('\nNuevo nombre: ').strip()

        # Valida que no esté vacío
        if not nuevo_nombre:
            print('El nombre no puede estar vacío.')
            continue

        # Valida que no contenga números
        if any(caracter.isdigit() for caracter in nuevo_nombre):
            print('El nombre no puede contener números.')
            continue
        
        # Verifica si ya existe otro país con ese nombre (coincidencia exacta)
        pais_duplicado = buscar_exacto(paises, nuevo_nombre)
        # Permite el mismo nombre solo si pertenece al país actual (evita choque con otro)
        if pais_duplicado and pais_duplicado['nombre'] != pais_actual['nombre']:
            print(f'Ya existe un país con el nombre "{pais_duplicado["nombre"]}".')
            continue
            
        # Devuelve el nombre con formato título (primera letra en mayúscula)
        return nuevo_nombre.title()


def solicitar_nuevo_continente():
    # Lista de continentes permitidos para la selección
    continentes = ['África', 'América del Norte', 'América del Sur', 'Asia', 'Europa', 'Oceanía']
    
    # Muestra las opciones numeradas
    print('\nContinentes disponibles:')
    for i, cont in enumerate(continentes, 1):
        print(f'  {i}) {cont}')
    
    # Bucle hasta que el usuario elija una opción válida
    while True:
        try:
            # Lee la opción numérica
            opcion = int(input('\nSeleccione el número: ').strip())
            # Valida que esté dentro del rango
            if 1 <= opcion <= len(continentes):
                # Devuelve el continente seleccionado
                return continentes[opcion - 1]
            else:
                print(f'Opción inválida. Debe elegir entre 1 y {len(continentes)}.')
        except ValueError:
            # Informa si no se ingresa un número válido
            print('Debes ingresar un número válido.')