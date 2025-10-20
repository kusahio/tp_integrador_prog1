import csv
import os

"""
Este módulo contiene funciones para agregar países al archivo CSV
"""

def guardar_pais_en_csv(ruta_archivo, pais):
    """
    Guarda un país en el archivo CSV.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV
        pais (dict): Diccionario con datos del país
    
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    try:
        # Verificar que el archivo existe
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
        
        # Abrir en modo append (agregar al final)
        with open(ruta_archivo, mode='a', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribir el país
            escritor.writerow(pais)
        
        return True
    
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"\nAVISO: {e}")
        return False
    
    except Exception as e:
        print(f"\nAVISO: Error al guardar en CSV - {e}")
        return False


def validar_nombre_unico(paises, nombre):
    """
    Verifica que el nombre del país no exista ya en la lista.
    
    Args:
        paises (list): Lista de países
        nombre (str): Nombre a validar
    
    Returns:
        bool: True si es único, False si ya existe
    """
    from funciones.filtros import quitar_tildes
    
    nombre_normalizado = quitar_tildes(nombre.lower().strip())
    
    for pais in paises:
        pais_normalizado = quitar_tildes(pais['nombre'].lower().strip())
        if nombre_normalizado == pais_normalizado:
            return False
    
    return True


def agregar_pais(paises, ruta_archivo="csv/paises_mundo.csv"):
    """
    Permite agregar un nuevo país de forma interactiva.
    Valida los datos y lo guarda tanto en memoria como en el CSV.
    
    Args:
        paises (list): Lista de países en memoria
        ruta_archivo (str): Ruta del archivo CSV donde guardar
    """
    print('\n' + '='*50)
    print('=== AGREGAR NUEVO PAÍS ===')
    print('='*50)
    
    try:
        # 1. VALIDAR NOMBRE
        while True:
            nombre = input('\nNombre del país: ').strip()
            
            # Validar que no esté vacío
            if not nombre:
                print('⚠ El nombre no puede estar vacío. Intente nuevamente.')
                continue
            
            # Validar que no contenga números
            if any(c.isdigit() for c in nombre):
                print('⚠ El nombre no puede contener números. Intente nuevamente.')
                continue
            
            # Validar que sea único
            if not validar_nombre_unico(paises, nombre):
                print(f'⚠ El país "{nombre}" ya existe en la base de datos.')
                continuar = input('¿Desea intentar con otro nombre? (s/n): ').lower().strip()
                if continuar != 's':
                    print('\nOperación cancelada.')
                    return
                continue
            
            # Nombre válido
            break
        
        # 2. VALIDAR POBLACIÓN
        while True:
            try:
                poblacion_input = input('Población: ').strip()
                poblacion = int(poblacion_input)
                
                if poblacion < 0:
                    print('⚠ La población no puede ser negativa. Intente nuevamente.')
                    continue
                
                # Población válida
                break
            
            except ValueError:
                print('⚠ Debe ingresar un número entero válido. Intente nuevamente.')
        
        # 3. VALIDAR SUPERFICIE
        while True:
            try:
                superficie_input = input('Superficie (km²): ').strip()
                superficie = int(superficie_input)
                
                if superficie < 0:
                    print('⚠ La superficie no puede ser negativa. Intente nuevamente.')
                    continue
                
                # Superficie válida
                break
            
            except ValueError:
                print('⚠ Debe ingresar un número entero válido. Intente nuevamente.')
        
        # 4. VALIDAR CONTINENTE
        continentes_validos = ['África', 'América', 'Asia', 'Europa', 'Oceanía']
        
        while True:
            print('\nContinentes disponibles:')
            for i, cont in enumerate(continentes_validos, 1):
                print(f'  {i}) {cont}')
            
            continente = input('Continente: ').strip()
            
            # Validar que no esté vacío
            if not continente:
                print('⚠ El continente no puede estar vacío. Intente nuevamente.')
                continue
            
            # Validar que no contenga números
            if any(c.isdigit() for c in continente):
                print('⚠ El continente no puede contener números. Intente nuevamente.')
                continue
            
            # Capitalizar primera letra
            continente = continente.capitalize()
            
            # Continente válido
            break
        
        # 5. MOSTRAR RESUMEN Y CONFIRMAR
        print('\n' + '-'*50)
        print('RESUMEN DEL PAÍS A AGREGAR:')
        print('-'*50)
        print(f'  Nombre      : {nombre}')
        print(f'  Población   : {poblacion:,} habitantes')
        print(f'  Superficie  : {superficie:,} km²')
        print(f'  Continente  : {continente}')
        print('-'*50)
        
        confirmacion = input('\n¿Confirma que desea agregar este país? (s/n): ').lower().strip()
        
        if confirmacion != 's':
            print('\n❌ Operación cancelada.')
            return
        
        nuevo_pais = {
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        }
        
        if guardar_pais_en_csv(ruta_archivo, nuevo_pais):
            paises.append(nuevo_pais)
            
            print('\n✓ ¡País agregado exitosamente!')
            print(f'  Total de países: {len(paises)}')
        else:
            print('\nAVISO: No se pudo guardar el país en el archivo CSV.')
    
    except KeyboardInterrupt:
        print('\n\nAVISO: Operación cancelada por el usuario.')
    
    except Exception as e:
        print(f'\nAVISO: Error inesperado: {e}')


def opcion_agregar_pais(paises, ruta_archivo="csv/paises_mundo.csv"):  
    while True:
        agregar_pais(paises, ruta_archivo)
        
        # Preguntar si desea agregar otro
        respuesta = input('\n¿Desea agregar otro país? (s/n): ').lower().strip()
        
        if respuesta != 's':
            print('\nVolviendo al menú principal...')
            break