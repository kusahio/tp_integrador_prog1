from funciones.estadistica import mostrar_estadisticas
from funciones.filtros import buscar_pais, filtrar_por_continente, filtrar_por_rango
from funciones.lectura import leer_csv
from funciones.menu import mostrar_menu
from funciones.ordenar import ordenar_paises

def main():
    paises = leer_csv("csv/paises_mundo.csv")
    if not paises:
        print("No se pudieron cargar datos. Revisa el archivo CSV.")
        return

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese el nombre del país: ")
            resultados = buscar_pais(paises, nombre)
            print(resultados if resultados else "No se encontraron coincidencias.")

        elif opcion == "2":
            continente = input("Ingrese el continente: ")
            resultados = filtrar_por_continente(paises, continente)
            print(resultados if resultados else "No hay países en ese continente.")

        elif opcion == "3":
            minimo = int(input("Ingrese población mínima: "))
            maximo = int(input("Ingrese población máxima: "))
            resultados = filtrar_por_rango(paises, "poblacion", minimo, maximo)
            print(resultados if resultados else "No se encontraron países en ese rango.")

        elif opcion == "4":
            minimo = int(input("Ingrese superficie mínima: "))
            maximo = int(input("Ingrese superficie máxima: "))
            resultados = filtrar_por_rango(paises, "superficie", minimo, maximo)
            print(resultados if resultados else "No se encontraron países en ese rango.")

        elif opcion == "5":
            clave = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            desc = input("¿Descendente? (s/n): ").lower() == "s"
            resultados = ordenar_paises(paises, clave, desc)
            for p in resultados:
                print(p)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")


main()
