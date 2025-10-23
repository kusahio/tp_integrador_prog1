from .utilidades import preguntar_si_no
from .filtros import buscar_exacto

def buscar_y_seleccionar_pais(paises, accion='editar'):
    nombre_buscar = input(f'Ingresa el nombre del país a {accion}: ').strip()
    
    if not nombre_buscar:
        print('\nEl nombre no puede estar vacío.')
        return None, None

    pais_encontrado = buscar_exacto(paises, nombre_buscar)

    if pais_encontrado is None:
        print(f'\nNo se encontró ningún país con el nombre exacto "{nombre_buscar}"')
        print('El nombre debe ser exacto (puedes omitir tildes y mayúsculas)')
        return None, None

    print(f'\nPaís encontrado: {pais_encontrado["nombre"]}')
    print('-' * 70)
    print(f'  Población  : {pais_encontrado["poblacion"]:,} habitantes')
    print(f'  Superficie : {pais_encontrado["superficie"]:,} km²')
    print(f'  Continente : {pais_encontrado["continente"]}')
    print('-' * 70)

    if not preguntar_si_no(f'\n¿Es este el país que deseas {accion}? (s/n): '):
        print('\nBúsqueda cancelada.')
        return None, None

    indice_pais = next((i for i, p in enumerate(paises) if p['nombre'] == pais_encontrado['nombre']), None)
    
    if indice_pais is None:
        print('\AVISO: no se encontró el país en la base de datos interna.')
        return None, None

    return pais_encontrado, indice_pais

def solicitar_valor_numerico(mensaje_prompt):
    while True:
        try:
            valor = int(input(mensaje_prompt).strip())
            if valor <= 0:
                print('El valor debe ser un número positivo.')
                continue
            return valor
        except ValueError:
            print('Debes ingresar un número entero válido.')

def solicitar_nuevo_nombre(paises, pais_actual):
    while True:
        nuevo_nombre = input('\nNuevo nombre: ').strip()
        if not nuevo_nombre:
            print('El nombre no puede estar vacío.')
            continue
        if any(c.isdigit() for c in nuevo_nombre):
            print('El nombre no puede contener números.')
            continue
        
        # Verificar si ya existe otro país con ese nombre
        pais_duplicado = buscar_exacto(paises, nuevo_nombre)
        if pais_duplicado and pais_duplicado['nombre'] != pais_actual['nombre']:
            print(f'Ya existe un país con el nombre "{pais_duplicado["nombre"]}".')
            continue
            
        return nuevo_nombre.title()

def solicitar_nuevo_continente():
    continentes = ['África', 'América del Norte', 'América del Sur', 'Asia', 'Europa', 'Oceanía']
    
    print('\nContinentes disponibles:')
    for i, cont in enumerate(continentes, 1):
        print(f'  {i}) {cont}')
    
    while True:
        try:
            opcion = int(input('\nSeleccione el número: ').strip())
            if 1 <= opcion <= len(continentes):
                return continentes[opcion - 1]
            else:
                print(f'Opción inválida. Debe elegir entre 1 y {len(continentes)}.')
        except ValueError:
            print('Debes ingresar un número válido.')