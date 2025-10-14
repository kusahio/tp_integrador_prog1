from funciones.lectura import leer_csv
from funciones.menu import mostrar_menu
from funciones.opciones_menu import (
    opcion_buscar_pais,
    opcion_filtrar_continente,
    opcion_filtrar_poblacion,
    opcion_filtrar_superficie,
    opcion_ordenar_paises,
    opcion_mostrar_estadisticas
)


def main():
    # Cargar datos del archivo CSV
    paises = leer_csv("csv/paises_mundo.csv")
    
    if not paises:
        print("No se pudieron cargar datos. Revisa el archivo CSV.")
        return

    # Bucle principal del menú
    while True:
        try:
            # Mostrar menú y obtener opción
            opcion = mostrar_menu()
            opcion_int = int(opcion) if opcion.isdigit() else 0

            # Ejecutar opción seleccionada
            match opcion_int:
                case 1:
                    opcion_buscar_pais(paises)
                
                case 2:
                    opcion_filtrar_continente(paises)
                
                case 3:
                    opcion_filtrar_poblacion(paises)
                
                case 4:
                    opcion_filtrar_superficie(paises)
                
                case 5:
                    opcion_ordenar_paises(paises)
                
                case 6:
                    opcion_mostrar_estadisticas(paises)
                
                case 7:
                    print("\n¡Gracias por usar el programa!")
                    print("Saliendo...")
                    break
                
                case _:
                    print('\nLa opción ingresada no es válida')
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario (Ctrl+C)")
            print("Saliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        # Pausa para que el usuario vea los resultados
        #input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()