from funciones.lectura import leer_csv
from funciones.menu import mostrar_menu
from funciones.opciones_menu import (
    opcion_buscar_pais,
    opcion_filtrar_continente,
    opcion_filtrar_poblacion,
    opcion_filtrar_superficie,
    opcion_ordenar_paises,
    opcion_mostrar_estadisticas,
    opcion_agregar_pais,
    opcion_editar_pais,
    opcion_eliminar_pais
)



def main():
    # Cargar datos del archivo CSV
    ruta = 'csv/paises_mundo.csv'
    paises = leer_csv(ruta)

    # Bucle principal del menú
    while True:
        try:
            # Mostrar menú y obtener la opción elegida por el usuario
            opcion = mostrar_menu()
            # Convierte a entero si la entrada es numérica; si no, usa 0 para forzar la opción inválida
            opcion_int = int(opcion) if opcion.isdigit() else 0

            # Ejecutar la opción seleccionada usando 'match' (requiere Python 3.10+)
            match opcion_int:
                case 1:
                    # Buscar país por nombre (búsqueda parcial)
                    opcion_buscar_pais(paises)
                
                case 2:
                    # Filtrar países por continente
                    opcion_filtrar_continente(paises)
                
                case 3:
                    # Filtrar por rango de población
                    opcion_filtrar_poblacion(paises)
                
                case 4:
                    # Filtrar por rango de superficie
                    opcion_filtrar_superficie(paises)
                
                case 5:
                    # Ordenar países por nombre/población/superficie
                    opcion_ordenar_paises(paises)
                
                case 6:
                    # Mostrar estadísticas generales
                    opcion_mostrar_estadisticas(paises)

                case 7:
                    # Agregar un nuevo país (actualiza lista y CSV)
                    opcion_agregar_pais(paises, ruta)

                case 8:
                    # Editar un país existente (actualiza lista y CSV)
                    opcion_editar_pais(paises, ruta)

                case 9:
                    # Eliminar un país (actualiza lista y CSV)
                    opcion_eliminar_pais(paises, ruta)

                case 10:
                    # Salir del programa
                    print('\n¡Gracias por usar el programa!')
                    print('Saliendo...')
                    break
                
                case _:
                    # Cualquier número fuera del rango válido
                    print('\nLa opción ingresada no es válida')
        
        # Error típico de conversión/validación dentro de las opciones
        except ValueError as e:
            print(f'Error: {e}')
        # Permite salir limpiamente con Ctrl+C
        except KeyboardInterrupt:
            print('\n\nPrograma interrumpido por el usuario (Ctrl+C)')
            print('Saliendo...')
            break
        # Cualquier otro error no previsto
        except Exception as e:
            print(f'Error inesperado: {e}')


# Punto de entrada del script: solo ejecuta main si el archivo se ejecuta directamente
if __name__ == '__main__':
    main()