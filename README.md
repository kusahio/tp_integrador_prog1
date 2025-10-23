# Gestión de Datos de Países en Python

## Descripción del programa

Este proyecto es una aplicación de consola desarrollada en **Python 3** que permite **gestionar información sobre países** a partir de un archivo CSV.  
Fue creado como **Trabajo Práctico Integrador** para la materia *Programación 1* de la *Tecnicatura Universitaria en Programación*.

El programa lee datos de países (nombre, población, superficie y continente) y ofrece funcionalidades de:
- Búsqueda por nombre (exacta o parcial)
- Filtros por continente, rango de población y rango de superficie
- Ordenamientos por nombre, población o superficie (ascendente o descendente)
- Cálculo de estadísticas (promedios, país con mayor/menor población, cantidad por continente)
- **Agregar nuevos países al sistema**
- **Editar información de países existentes**
- **Eliminar países de la base de datos**
- Visualización paginada de resultados con navegación interactiva

Todo el sistema está modularizado, validado y cuenta con manejo robusto de errores.

---

## Instrucciones de uso

### Requisitos previos
- Tener instalado **Python 3.10 o superior**
- Tener instalado **Git** en tu sistema

### Instalación

1. **Clonar el repositorio desde GitHub**

   Abre una terminal o línea de comandos y ejecuta:

   ```bash
   git clone https://github.com/kusahio/tp_integrador_prog1.git
   ```

2. **Navegar a la carpeta del proyecto**

   ```bash
   cd tp_integrador_prog1
   ```

3. **Verificar la estructura del proyecto**

   Asegúrate de que la estructura sea la siguiente:

   ```
   tp_integrador_prog1/
   │
   ├── main.py
   ├── README.md
   │
   ├── csv/
   │   └── paises_mundo.csv
   │
   └── funciones/
       ├── __init__.py
       ├── lectura.py
       ├── filtros.py
       ├── ordenar.py
       ├── estadistica.py
       ├── paginador.py
       ├── menu.py
       ├── opciones_menu.py
       ├── edicion.py
       ├── auxiliares.py
       └── utilidades.py
   ```

4. **Ejecutar el programa**

   ```bash
   python main.py
   ```

### Navegación por el menú

Al ejecutar el programa, se mostrará el menú principal:

```
==== MENÚ PRINCIPAL ====

1) Buscar país por nombre
2) Filtrar países por continente
3) Filtrar por rango de población
4) Filtrar por rango de superficie
5) Ordenar países
6) Mostrar estadísticas
7) Agregar país
8) Editar país
9) Eliminar país
10) Salir
```

El usuario debe ingresar el número correspondiente a la opción deseada y seguir las instrucciones que aparecen por consola.

---

## Ejemplos de entradas y salidas

### Ejemplo 1: Buscar país por nombre

**Entrada:**
```
Ingrese un número de opción: 1
Ingrese el nombre del país: arg
```

**Salida:**
```
======================================================================
Países que coinciden con "arg"
Mostrando 2 resultados
======================================================================

  1. Argentina - América del Sur
  2. Argelia - África

----------------------------------------------------------------------
Presione Enter para continuar...

¿Buscar otro país? (s/n): n
```

**Características:**
- Búsqueda insensible a mayúsculas y tildes
- Coincidencia parcial (buscar "arg" encuentra "Argentina")
- Con 1 solo resultado, muestra formato simplificado sin paginación
- Opción de realizar múltiples búsquedas sin volver al menú principal

---

### Ejemplo 2: Filtrar países por continente

**Entrada:**
```
Ingrese un número de opción: 2
Ingrese el continente: Europa
```

**Salida:**
```
======================================================================
Países en Europa
Página 1 de 5 | Mostrando 1-10 de 44 resultados
======================================================================

  1. Albania - Europa
  2. Alemania - Europa
  3. Andorra - Europa
  4. Austria - Europa
  5. Bélgica - Europa
  6. Bielorrusia - Europa
  7. Bosnia y Herzegovina - Europa
  8. Bulgaria - Europa
  9. Chipre - Europa
  10. Croacia - Europa

----------------------------------------------------------------------
Enter = Siguiente | A = Anterior | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------

Seleccione una opción: 
```

**Características:**
- Navegación paginada con 10 resultados por página
- Controles interactivos: Enter (siguiente), A (anterior), número (ir a página específica), S (salir)
- Filtrado insensible a mayúsculas y tildes
- Opción de filtrar por otro continente al finalizar

---

### Ejemplo 3: Filtrar por rango de población

**Entrada:**
```
Ingrese un número de opción: 3
Ingrese población mínima: 1000000
Ingrese población máxima: 5000000
```

**Salida:**
```
======================================================================
Países con población entre 1,000,000 y 5,000,000
Página 1 de 2 | Mostrando 1-10 de 15 resultados
======================================================================

  1. Uruguay: 3,473,730 habitantes
  2. Panamá: 4,314,768 habitantes
  3. Costa Rica: 5,094,114 habitantes
  4. Irlanda: 4,937,786 habitantes
  5. Nueva Zelanda: 4,822,233 habitantes
  6. Noruega: 5,421,241 habitantes
  7. Singapur: 5,850,342 habitantes
  8. Dinamarca: 5,792,202 habitantes
  9. Finlandia: 5,540,720 habitantes
  10. República Centroafricana: 4,829,767 habitantes

----------------------------------------------------------------------
Enter = Siguiente | A = Anterior | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------

Seleccione una opción: 2
```

**Características:**
- Formato de números con separadores de miles para mejor legibilidad
- Validación de rangos (mínimo no puede ser mayor que máximo)
- Validación de valores positivos
- Navegación directa a cualquier página ingresando su número

---

### Ejemplo 4: Filtrar por rango de superficie

**Entrada:**
```
Ingrese un número de opción: 4
Ingrese superficie mínima (km²): 500000
Ingrese superficie máxima (km²): 1000000
```

**Salida:**
```
======================================================================
Países con superficie entre 500,000 y 1,000,000 km²
Mostrando 5 resultados
======================================================================

  1. Pakistán: 881,912 km²
  2. Namibia: 825,615 km²
  3. Mozambique: 801,590 km²
  4. Turquía: 783,562 km²
  5. Chile: 756,102 km²

----------------------------------------------------------------------
Presione Enter para continuar...

¿Filtrar otro rango de superficie? (s/n): n
```

**Características:**
- Muestra superficie en km² con formato legible
- Validación de entrada numérica
- Opción de repetir el filtrado con diferentes valores

---

### Ejemplo 5: Ordenar países

**Entrada:**
```
Ingrese un número de opción: 5

Opciones de ordenamiento:
  - nombre
  - poblacion
  - superficie

Ordenar por: poblacion
¿Descendente? (s/n): s
```

**Salida:**
```
======================================================================
Países ordenados por poblacion (descendente)
Página 1 de 20 | Mostrando 1-10 de 195 resultados
======================================================================

  1. China: 1,439,323,776 habitantes
  2. India: 1,380,004,385 habitantes
  3. Estados Unidos: 331,002,651 habitantes
  4. Indonesia: 273,523,615 habitantes
  5. Pakistán: 220,892,340 habitantes
  6. Brasil: 212,559,417 habitantes
  7. Nigeria: 206,139,589 habitantes
  8. Bangladesh: 164,689,383 habitantes
  9. Rusia: 145,934,462 habitantes
  10. México: 128,932,753 habitantes

----------------------------------------------------------------------
Enter = Siguiente | A = Anterior | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------

Seleccione una opción: 
```

**Opciones de ordenamiento:**
- **Por nombre**: Orden alfabético (A-Z o Z-A)
- **Por población**: Del más poblado al menos poblado (o viceversa)
- **Por superficie**: Del más grande al más pequeño (o viceversa)

**Características:**
- Formato de visualización adaptado al tipo de ordenamiento
- Cuando se ordena por población, muestra la cantidad de habitantes
- Cuando se ordena por superficie, muestra los km²
- Cuando se ordena por nombre, muestra el formato simple con continente
- Opción de ordenar múltiples veces con diferentes criterios

---

### Ejemplo 6: Mostrar estadísticas

**Entrada:**
```
Ingrese un número de opción: 6
```

**Salida:**
```
==== ESTADÍSTICAS ==== 
- País con mayor población  : China (1,439,323,776)
- País con menor población  : Vaticano (801)
- Promedio de población     : 39,265,489
- Promedio de superficie    : 695,652

Cantidad de países por continente:
  - África: 54
  - América: 35
  - Asia: 48
  - Europa: 44
  - Oceanía: 14
```

**Estadísticas incluidas:**
- País con mayor población y su cantidad de habitantes
- País con menor población y su cantidad de habitantes
- Promedio de población mundial
- Promedio de superficie territorial
- Distribución de países por continente

---

### Ejemplo 7: Agregar país

**Entrada:**
```
Ingrese un número de opción: 7

==== Agregar nuevo país ====

Ingrese nombre del país: luxemburgo
Ingrese la población del país: 634730
Ingrese la superficie del país (km²): 2586

Continentes disponibles:
  1) África
  2) América del Norte
  3) América del Sur
  4) Asia
  5) Europa
  6) Oceanía

Ingresa el número de opción del continente del país: 5
```

**Salida:**
```
--------------------------------------------------
Resumen del país que vas a agregar:
--------------------------------------------------
  Nombre      : Luxemburgo
  Población   : 634,730 habitantes
  Superficie  : 2,586 km²
  Continente  : Europa
--------------------------------------------------

¿Confirma que desea agregar este país? (s/n): s

✓ ¡País agregado exitosamente!
  Total de países: 196

¿Desea agregar otro país? (s/n): n
```

**Validaciones implementadas:**

**Entrada inválida - Campo vacío:**
```
Ingrese nombre del país: 

AVISO: El nombre no puede estar vacío

¿Desea intentar nuevamente? (s/n): s
```

**Entrada inválida - Nombre con números:**
```
Ingrese nombre del país: pais123

AVISO: El nombre no puede contener números

¿Desea intentar nuevamente? (s/n): s
```

**Entrada inválida - País duplicado:**
```
Ingrese nombre del país: argentina

AVISO: El país "Argentina" ya existe!

¿Desea intentar nuevamente? (s/n): s
```

**Entrada inválida - Población no numérica:**
```
Ingrese la población del país: abc

AVISO: La población debe ser un número entero

¿Desea intentar nuevamente? (s/n): s
```

**Entrada inválida - Población negativa o cero:**
```
Ingrese la población del país: -500

AVISO: La población debe ser mayor a 0

¿Desea intentar nuevamente? (s/n): s
```

**Entrada inválida - Opción de continente fuera de rango:**
```
Ingresa el número de opción del continente del país: 10

AVISO: La opción está fuera de rango

¿Desea intentar nuevamente? (s/n): s
```

**Características:**
- Validación exhaustiva en cada campo
- Sistema de normalización de nombres (capitalización automática)
- Verificación de duplicados (insensible a tildes y mayúsculas)
- Resumen completo antes de confirmar
- Opción de cancelar en cualquier momento
- Persistencia automática en el archivo CSV
- Contador actualizado del total de países

---

### Ejemplo 8: Editar país

**Entrada:**
```
Ingrese un número de opción: 8

==== Editar País ====

Ingresa el nombre del país a editar: argentina
```

**Salida:**
```
País encontrado: Argentina
----------------------------------------------------------------------
  Población  : 45,195,774 habitantes
  Superficie : 2,780,400 km²
  Continente : América del Sur
----------------------------------------------------------------------

¿Es este el país que deseas editar? (s/n): s

¿Qué campos deseas editar?

  1) Nombre
  2) Población
  3) Superficie
  4) Continente
  5) Todo
  6) Cancelar

Opción: 2

Nueva población: 46000000
¿Confirma el cambio? (s/n): s

Campo 'poblacion' actualizado correctamente

  Anterior: 45195774
  Nuevo   : 46000000

Población actualizada correctamente.

¿Desea editar otro país? (s/n): n
```

**Opción de editar todos los campos:**

**Entrada:**
```
Opción: 5

==== Ingrese los Nuevos Datos ====

Nuevo nombre: República Argentina
Nueva población: 46500000
Nueva superficie (km²): 2780400

Continentes disponibles:
  1) África
  2) América del Norte
  3) América del Sur
  4) Asia
  5) Europa
  6) Oceanía

Seleccione el número: 3
```

**Salida:**
```
Resumen de cambios:
----------------------------------------------------------------------
  Nombre      : Argentina --> República Argentina
  Población   : 45,195,774 --> 46,500,000
  Superficie  : 2,780,400 --> 2,780,400 km²
  Continente  : América del Sur --> América del Sur
----------------------------------------------------------------------

¿Confirma los cambios? (s/n): s

¡País actualizado correctamente!

¿Desea editar otro país? (s/n): n
```

**Validaciones implementadas:**

**Entrada inválida - País no encontrado:**
```
Ingresa el nombre del país a editar: paisinventado

No se encontró ningún país con el nombre exacto "paisinventado"
El nombre debe ser exacto (puedes omitir tildes y mayúsculas)

¿Desea intentar con otro nombre? (s/n): s
```

**Entrada inválida - Campo vacío:**
```
Ingresa el nombre del país a editar: 

El nombre no puede estar vacío.

¿Desea intentar con otro nombre? (s/n): s
```

**Entrada inválida - Opción de menú inválida:**
```
Opción: 99

Opción inválida. Debe elegir entre 1 y 6.

¿Desea editar otro país? (s/n): n
```

**Entrada inválida - Nuevo nombre duplicado:**
```
Nuevo nombre: Brasil

Ya existe un país con el nombre "Brasil".

Nuevo nombre: 
```

**Entrada inválida - Nombre con números:**
```
Nuevo nombre: Argentina123

El nombre no puede contener números.

Nuevo nombre: 
```

**Entrada inválida - Valor numérico inválido:**
```
Nueva población: abc

Debes ingresar un número entero válido.

Nueva población: 
```

**Entrada inválida - Valor negativo:**
```
Nueva población: -1000

El valor debe ser un número positivo.

Nueva población: 
```

**Características:**
- Búsqueda exacta con normalización (insensible a tildes y mayúsculas)
- Visualización completa de la información actual del país
- Edición individual de campos o todos a la vez
- Resumen de cambios antes de confirmar
- Validación de nombres duplicados
- Confirmación adicional para evitar cambios accidentales
- Opción de cancelar en cualquier momento
- Los cambios se guardan automáticamente en el CSV
- Reversión automática si falla el guardado

---

### Ejemplo 9: Eliminar país

**Entrada:**
```
Ingrese un número de opción: 9

==== Eliminar País ====

Ingresa el nombre del país a eliminar: vaticano
```

**Salida:**
```
País encontrado: Vaticano
----------------------------------------------------------------------
  Población  : 801 habitantes
  Superficie : 0 km²
  Continente : Europa
----------------------------------------------------------------------

¿Es este el país que deseas eliminar? (s/n): s

AVISO: Estás a punto de eliminar a "Vaticano" de forma permanente.
¿Estás realmente seguro de que deseas continuar? (s/n): s

El país "Vaticano" ha sido eliminado exitosamente.
Total de países restantes: 194

¿Desea eliminar otro país? (s/n): n
```

**Validaciones implementadas:**

**Entrada inválida - País no encontrado:**
```
Ingresa el nombre del país a eliminar: atlantida

No se encontró ningún país con el nombre exacto "atlantida"
El nombre debe ser exacto (puedes omitir tildes y mayúsculas)

¿Deseas intentar con otro nombre? (s/n): s
```

**Entrada inválida - Campo vacío:**
```
Ingresa el nombre del país a eliminar: 

El nombre no puede estar vacío.

¿Deseas intentar con otro nombre? (s/n): s
```

**Usuario cancela la eliminación:**
```
¿Es este el país que deseas eliminar? (s/n): n

Búsqueda cancelada.

¿Deseas intentar con otro nombre? (s/n): n
```

**Usuario cancela después de ver el aviso:**
```
AVISO: Estás a punto de eliminar a "Vaticano" de forma permanente.
¿Estás realmente seguro de que deseas continuar? (s/n): n

Operación de eliminación cancelada.

¿Desea eliminar otro país? (s/n): n
```

**Error al guardar cambios (reversión automática):**
```
AVISO: No se pudieron guardar los cambios. La eliminación ha sido revertida.

¿Desea eliminar otro país? (s/n): n
```

**Características:**
- Búsqueda exacta con normalización (insensible a tildes y mayúsculas)
- Visualización completa de la información del país antes de eliminar
- Doble confirmación para evitar eliminaciones accidentales
- Mensaje de advertencia claro sobre la permanencia de la acción
- Contador actualizado del total de países restantes
- Reversión automática si falla el guardado en CSV
- Opción de eliminar múltiples países en una sesión
- Búsqueda insensible a mayúsculas y tildes para facilitar la localización

---

### Ejemplo 10: Manejo de errores

**Entrada inválida - Opción de menú:**
```
Ingrese un número de opción: 99

La opción ingresada no es válida
```

**Entrada inválida - Búsqueda con números:**
```
Ingrese el nombre del país: arg123

AVISO: El nombre no puede contener números. Intente nuevamente.

Ingrese el nombre del país: 
```

**Entrada inválida - Rango de población:**
```
Ingrese población mínima: 5000000
Ingrese población máxima: 1000000

AVISO: El mínimo no puede ser mayor que el máximo. Intente nuevamente.

Ingrese población mínima: 
```

**Entrada inválida - Campo vacío:**
```
Ingrese el continente: 

AVISO: El continente no puede estar vacío. Intente nuevamente.

Ingrese el continente: 
```

**Características del manejo de errores:**
- Validación de tipos de datos (números, texto)
- Validación de rangos lógicos
- Validación de campos vacíos
- Mensajes descriptivos que indican el problema
- Opción de reintentar sin salir de la función
- Prevención de errores de ejecución
- Protección contra duplicados
- Validación de integridad de datos

---

### Ejemplo 11: Navegación en el paginador

**El sistema de paginación es adaptativo según la cantidad de resultados:**

#### Caso 1: 10 o menos resultados (1 página)
```
======================================================================
Países que coinciden con "br"
Mostrando 3 resultados
======================================================================

  1. Brasil - América del Sur
  2. Brunéi - Asia

----------------------------------------------------------------------
Presione Enter para continuar...
```
*No hay navegación de páginas, solo Enter para continuar*

---

#### Caso 2: Entre 11 y 20 resultados (2 páginas)

**Primera página:**
```
----------------------------------------------------------------------
Enter = Siguiente | S = Salir
----------------------------------------------------------------------
```

**Segunda página:**
```
----------------------------------------------------------------------
Enter = Volver a página 1 | A = Anterior | S = Salir
----------------------------------------------------------------------
```

*Controles: Enter (siguiente/volver), A (anterior), S (salir)*  
*No está disponible ir a página específica con solo 2 páginas*

---

#### Caso 3: Más de 20 resultados (3+ páginas)

**Primera página:**
```
----------------------------------------------------------------------
Enter = Siguiente | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------
```

**Páginas intermedias:**
```
----------------------------------------------------------------------
Enter = Siguiente | A = Anterior | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------
```

**Última página:**
```
----------------------------------------------------------------------
Enter = Volver a página 1 | A = Anterior | [Número] = Ir a página | S = Salir
----------------------------------------------------------------------
```

*Controles completos: Enter, A (anterior), número específico, S (salir)*

---

**Ejemplos de navegación:**

```
Seleccione una opción: 5
```
*(Salta directamente a la página 5 - solo disponible con 3+ páginas)*

```
Seleccione una opción: a
```
*(Retrocede a la página anterior - disponible desde página 2 en adelante)*

```
Seleccione una opción: 
```
*(Presionar Enter avanza a la siguiente página, o vuelve a página 1 si estás en la última)*

```
Seleccione una opción: s
```
*(Sale del paginador - disponible con 2+ páginas)*

**Características especiales:**
- En la última página, Enter vuelve automáticamente a la página 1 (navegación circular)
- Los controles se adaptan inteligentemente según el contexto
- Con solo 1 página, no hay controles de navegación, solo continuar
- La opción de ir a página específica solo aparece con 3+ páginas

---

## Participación de los integrantes

**Integrante 1:** Camilo Illanes  
- Estructura general del proyecto  
- Módulos `lectura.py`, `filtros.py`, `menu.py`, `paginador.py`
- Sistema de paginación interactivo con navegación completa
- Pruebas de funcionamiento y validaciones
- Sistema de búsqueda con normalización de texto (tildes y mayúsculas)
- Manejo de errores y excepciones
- Módulos `edicion.py`, `auxiliares.py` y `utilidades.py`
- Funcionalidades de agregar, editar y eliminar países
- Sistema de validaciones para operaciones CRUD
- Persistencia de datos en CSV con manejo de errores

**Integrante 2:** Rafael Ruiz  
- Módulos `ordenar.py`, `estadistica.py`, `opciones_menu.py`
- Cálculo de estadísticas descriptivas
- Formatos de visualización múltiples
- Documentación interna y depuración
- Integración de nuevas opciones al menú principal
- Testing de funcionalidades de edición

**Trabajo colaborativo:**
- Integración y testing del sistema completo
- Diseño de la interfaz de usuario
- Validaciones exhaustivas en todas las funciones
- Preparación de la presentación y documentación
- Pruebas de persistencia de datos
- Validación de integridad en operaciones CRUD

---

## Tecnologías y conceptos aplicados

- **Python 3.10+**: Lenguaje de programación principal
- **Módulos nativos**: `csv`, `os`, `unicodedata`
- **Estructuras de datos**: Listas y diccionarios
- **Funciones**: Modularización y reutilización de código
- **Funciones lambda**: Para ordenamiento personalizado
- **List comprehensions**: Para filtrado eficiente
- **Match-case**: Control de flujo del menú (Python 3.10+)
- **Manejo de excepciones**: Try-except para control robusto de errores
- **Algoritmos de ordenamiento**: Función `sorted()` con key personalizada
- **Estadística descriptiva**: Cálculo de máximos, mínimos y promedios
- **Validación de entrada**: Control de tipos y rangos
- **Normalización de texto**: Manejo de tildes y mayúsculas/minúsculas
- **Paginación**: Sistema de navegación para grandes conjuntos de datos
- **CRUD completo**: Create, Read, Update, Delete de registros
- **Persistencia de datos**: Lectura y escritura en archivos CSV
- **Manejo de archivos**: Operaciones seguras con verificación de existencia
- **Validación de duplicados**: Verificación de unicidad en nombres
- **Reversión de cambios**: Rollback automático en caso de errores

---

## Funcionalidades implementadas

### Obligatorias
- [x] Búsqueda de países por nombre
- [x] Filtrado por continente
- [x] Filtrado por rango de población
- [x] Filtrado por rango de superficie
- [x] Ordenamiento por nombre, población y superficie
- [x] Estadísticas: mayor/menor población, promedios, conteo por continente
- [x] Validaciones y manejo de errores
- [x] Código modular y comentado

### Extras implementados
- [x] **Sistema completo CRUD** (Create, Read, Update, Delete)
- [x] **Agregar países**: Con validación exhaustiva de todos los campos
- [x] **Editar países**: Edición individual de campos o todos a la vez
- [x] **Eliminar países**: Con doble confirmación y reversión automática
- [x] **Búsqueda exacta**: Para operaciones de edición y eliminación
- [x] **Validación de duplicados**: Prevención de nombres repetidos
- [x] **Persistencia automática**: Guardado inmediato en CSV
- [x] **Reversión de cambios**: Rollback si falla el guardado
- [x] **Confirmaciones múltiples**: Para evitar cambios accidentales
- [x] Sistema de paginación interactivo **adaptativo** según cantidad de resultados
- [x] Navegación inteligente: los controles cambian según el contexto (1, 2 o 3+ páginas)
- [x] Navegación circular: en la última página, Enter vuelve a la primera
- [x] Tres modos de paginación:
  - **Modo simple**: ≤10 resultados, solo continuar
  - **Modo básico**: 11-20 resultados (2 páginas), navegación siguiente/anterior/salir
  - **Modo completo**: 21+ resultados (3+ páginas), navegación completa con salto a página específica
- [x] Búsqueda insensible a mayúsculas y tildes
- [x] Múltiples formatos de visualización (simple, población, superficie, completo)
- [x] Mensajes de error descriptivos y específicos
- [x] Opción de repetir operaciones sin volver al menú principal
- [x] Formato de números con separadores de miles
- [x] Validaciones exhaustivas en cada entrada
- [x] Control de Ctrl+C para salida segura del programa
- [x] **Resúmenes informativos**: Antes de confirmar agregar o editar
- [x] **Contador de registros**: Actualización automática del total de países
- [x] **Validación de archivos**: Creación automática si no existe el CSV

---

## Notas adicionales

- El programa maneja correctamente caracteres especiales y tildes en nombres de países
- Los resultados se muestran formateados con separadores de miles para mejor legibilidad
- El sistema de paginación se adapta automáticamente según la cantidad de resultados:
  - **1-10 resultados**: Sin paginación, solo presionar Enter
  - **11-20 resultados**: Paginación básica con 2 páginas
  - **21+ resultados**: Paginación completa con salto a páginas específicas
- Todas las entradas son validadas para prevenir errores de ejecución
- Se puede interrumpir el programa con Ctrl+C de forma segura
- Los controles del paginador se adaptan según la página actual y total de páginas
- En la última página, Enter vuelve automáticamente a la primera (navegación circular)
- El formato de visualización cambia automáticamente según el tipo de consulta
- **Las operaciones de agregar, editar y eliminar se guardan automáticamente en el CSV**
- **Sistema de validación de duplicados** que considera nombres sin tildes y mayúsculas
- **Doble confirmación en eliminaciones** para evitar pérdida accidental de datos
- **Reversión automática** si falla el guardado de cambios
- **Búsqueda exacta normalizada** facilita encontrar países para editar o eliminar
- **Resúmenes antes de confirmar** permiten revisar los cambios antes de aplicarlos
- Si el archivo CSV no existe, se crea automáticamente con los encabezados correctos
- Los campos numéricos solo aceptan valores enteros positivos
- **Edición selectiva**: Permite modificar solo los campos necesarios sin tocar el resto
- **Visualización previa**: Muestra todos los datos del país antes de editarlo o eliminarlo

---

## Conclusión

Este proyecto permitió afianzar los conocimientos de estructuras de datos, modularización y buenas prácticas en Python, aplicando un caso real de manipulación de datos con un **sistema CRUD completo**.

El trabajo en equipo y la planificación modular facilitaron la integración de funciones complejas como ordenamientos, estadísticas y **operaciones de persistencia de datos** sin perder legibilidad ni control del flujo principal.

La implementación de las funcionalidades de **agregar, editar y eliminar países** añadió una capa completa de gestión de datos, convirtiendo el sistema en una aplicación funcional de administración de información con validaciones robustas y manejo seguro de archivos.

---

**Materia:** Programación 1  
**Carrera:** Tecnicatura Universitaria en Programación  
**Institución:** UTN – Universidad Tecnológica Nacional - Facultad Regional Mendoza