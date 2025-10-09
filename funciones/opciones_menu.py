from funciones.filtros import buscar_pais, filtrar_por_continente, filtrar_por_rango
from funciones.ordenar import ordenar_paises
from funciones.estadistica import mostrar_estadisticas

"""
Funciones internas utilizadas en este archivo:
    isinstance(objeto, tipo): Sirve para verificar el tipo de dato de una variable u objeto
    raise: Sirve para lanzar una excepción (error) de forma manual
"""


def opcion_buscar_pais(paises):
    # Opción 1: Buscar país por nombre
    try:
        nombre = input("Ingrese el nombre del país: ")
        
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        resultados = buscar_pais(paises, nombre)
        
        if resultados:
            print(f"\n==== Se encontraron {len(resultados)} resultado(s) ====")
            for pais in resultados:
                print(f"  • {pais['nombre']} - {pais['continente']}")
        else:
            print("No se encontraron coincidencias.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def opcion_filtrar_continente(paises):
    # Opción 2: Filtrar países por continente
    try:
        continente = input("Ingrese el continente: ")
        
        if not continente.strip():
            raise ValueError("El continente no puede estar vacío")
        
        resultados = filtrar_por_continente(paises, continente)
        
        if resultados:
            print(f"\n==== Países en {continente}: {len(resultados)} ====")
            for pais in resultados:
                print(f"  • {pais['nombre']}")
        else:
            print(f"No hay países en el continente '{continente}'.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def opcion_filtrar_poblacion(paises):
    # Opción 3: Filtrar países por rango de población
    try:
        minimo_str = input("Ingrese población mínima: ")
        maximo_str = input("Ingrese población máxima: ")
        
        if not minimo_str.strip() or not maximo_str.strip():
            raise ValueError("Los valores no pueden estar vacíos")
        
        if not minimo_str.isdigit() or not maximo_str.isdigit():
            raise ValueError("Debe ingresar números enteros positivos")
        
        minimo = int(minimo_str)
        maximo = int(maximo_str)
        
        if minimo < 0 or maximo < 0:
            raise ValueError("Los valores deben ser positivos")
        
        if minimo > maximo:
            raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        
        resultados = filtrar_por_rango(paises, "poblacion", minimo, maximo)
        
        if resultados:
            print(f"\n==== Países con población entre {minimo:,} y {maximo:,}: {len(resultados)} ====")
            for pais in resultados:
                print(f"  • {pais['nombre']}: {pais['poblacion']:,} habitantes")
        else:
            print("No se encontraron países en ese rango de población.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def opcion_filtrar_superficie(paises):
    # Opción 4: Filtrar países por rango de superficie
    try:
        minimo_str = input("Ingrese superficie mínima (km²): ")
        maximo_str = input("Ingrese superficie máxima (km²): ")
        
        if not minimo_str.strip() or not maximo_str.strip():
            raise ValueError("Los valores no pueden estar vacíos")
        
        if not minimo_str.isdigit() or not maximo_str.isdigit():
            raise ValueError("Debe ingresar números enteros positivos")
        
        minimo = int(minimo_str)
        maximo = int(maximo_str)
        
        if minimo < 0 or maximo < 0:
            raise ValueError("Los valores deben ser positivos")
        
        if minimo > maximo:
            raise ValueError("El valor mínimo no puede ser mayor que el máximo")
        
        resultados = filtrar_por_rango(paises, "superficie", minimo, maximo)
        
        if resultados:
            print(f"\n==== Países con superficie entre {minimo:,} y {maximo:,} km²: {len(resultados)} ====")
            for pais in resultados:
                print(f"  • {pais['nombre']}: {pais['superficie']:,} km²")
        else:
            print("No se encontraron países en ese rango de superficie.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def opcion_ordenar_paises(paises):
    # Opción 5: Ordenar países por diferentes criterios
    try:
        print("\nOpciones de ordenamiento:")
        print("  - nombre")
        print("  - poblacion")
        print("  - superficie")
        
        clave = input("Ordenar por: ").lower().strip()
        
        if not clave:
            raise ValueError("Debe ingresar una opción de ordenamiento")
        
        claves_validas = ["nombre", "poblacion", "superficie"]
        if clave not in claves_validas:
            raise ValueError(f"Opción inválida. Use: {', '.join(claves_validas)}")
        
        desc_input = input("¿Descendente? (s/n): ").lower().strip()
        
        if desc_input not in ["s", "n"]:
            raise ValueError("Debe ingresar 's' para sí o 'n' para no")
        
        desc = desc_input == "s"
        
        resultados = ordenar_paises(paises, clave, desc)
        
        if resultados:
            orden = "descendente" if desc else "ascendente"
            print(f"\n==== Países ordenados por {clave} ({orden}) ====")
            for i, pais in enumerate(resultados[:10], 1):  # Mostrar solo los primeros 10
                valor = pais[clave]
                if isinstance(valor, int):
                    print(f"  {i}. {pais['nombre']}: {valor:,}")
                else:
                    print(f"  {i}. {pais['nombre']}: {valor}")
            
            if len(resultados) > 10:
                print(f"  ... y {len(resultados) - 10} más")
        else:
            print("\nNo hay países para ordenar.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def opcion_mostrar_estadisticas(paises):
    # Opción 6: Mostrar estadísticas generales
    try:
        mostrar_estadisticas(paises)
    except Exception as e:
        print(f"Error al mostrar estadísticas: {e}")