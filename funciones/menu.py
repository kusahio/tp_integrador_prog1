
def mostrar_menu():
    # Muestra el título del menú principal
    print('\n==== MENÚ PRINCIPAL ====\n')
    
    # Lista de opciones disponibles para el usuario
    print('1) Buscar país por nombre')
    print('2) Filtrar países por continente')
    print('3) Filtrar por rango de población')
    print('4) Filtrar por rango de superficie')
    print('5) Ordenar países')
    print('6) Mostrar estadísticas')
    print('7) Agregar país')
    print('8) Editar país')
    print('9) Eliminar país')
    print('10) Salir')
    
    # Solicita al usuario que ingrese el número de la opción elegida
    return input('\nIngrese un número de opción: ')