import csv
import os
def guardar_pais(ruta_archivo, pais):
    try:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError("No se encontro el archivo.")
        with open(ruta_archivo, mode = 'a', newline = '', enconding = 'utf-8') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escribir = csv.DictReader(archivo, fieldnames = campos)
            escribir.writerow(pais)
        return True
    except FileNotFoundError:
        print("No se encontro el archivo.")
        return False
    
def agregar_pais(paises, ruta_archivo):

    try:
        nombre = input("Ingrese nombre del pais: ").strip().lower()
        if not nombre:
            raise ValueError("El nombre no puede estar vacio.")
        if any(caracter.isdigit() for caracter in nombre):
            raise TypeError("El nombre no puede contener numeros.")
        poblacion = int(input("Ingrese la poblacion del pais: "))
        if not poblacion:
            raise ValueError("El campo no puede estar vacio.")
        if isinstance(poblacion, int):
            raise TypeError("La poblacion debe ser numerica.")
        
        superficie = int(input("Ingrese la poblacion del pais: "))
        if not superficie:
            raise ValueError("El campo no puede estar vacio.")
        if isinstance(superficie, int):
            raise TypeError("La poblacion debe ser numerica.")
        while True:
            continente = input("Ingrese continente del pais: ").strip().lower()
            if not continente:
                raise ValueError("El campo no puede estar vacio.")
            if any(caracter.isdigit() for caracter in continente):
                raise TypeError("El continente no puede ser numerico.")
            continentes = ("asia", "america del norte", "america del sur", "oceania", "europa", "africa")
        
            if continente not in continentes:
                print(f"El continente debe ser {', '.join(continentes)}")
            else: 
                break
        pais = {
            'nombre': nombre, 
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        }
        guardar_pais(ruta_archivo, pais)    
    except (ValueError, TypeError) as e:
        print(f"AVISO: {e}. Intenta nuevamente.")
