# Gestión de Datos de Países en Python: Filtros, Ordenamientos y Estadísticas

Aplicación de consola desarrollada en **Python 3** para el **Trabajo Práctico Integrador (TPI)** de la asignatura **Programación 1** (Tecnicatura Universitaria en Programación a Distancia — Universidad Tecnológica Nacional). El sistema permite administrar, consultar y analizar información demográfica y territorial de países almacenada en un archivo CSV (`paises.csv`), incorporando validaciones preventivas y persistencia automática.

## Datos Institucionales y del Estudiante

* **Institución:** Universidad Tecnológica Nacional (UTN)
* **Carrera:** Tecnicatura Universitaria en Programación a Distancia
* **Asignatura:** Programación 1
* **Apellido y Nombre:** Pazquier Renzo
* **Comisión:** Comisión 3
* **Docente:** Cintia Rigoni
* **Fecha de Entrega:** 16 de noviembre de 2026

## Enlaces de Entrega

* **Repositorio en GitHub:** https://github.com/renzo8350-bit/TPI_Programaci-n_1
* **Video Demostrativo (YouTube):** https://youtu.be/shOtWv3f4Jw
* **Documentación Académica y Técnica (PDF):** [`documentacion_tpi.pdf`](./documentacion_tpi.pdf) (incluida en la raíz del repositorio)

---

## Estructura del Proyecto

Todos los archivos del proyecto deben ubicarse al mismo nivel dentro de la carpeta raíz:

```text
.
├── main.py                 # Menú interactivo de consola y validación de entradas del usuario
├── datos_csv.py            # Lectura, validación estructural y persistencia en paises.csv
├── gestor_paises.py        # Lógica de negocio: altas, ediciones, búsquedas, filtros, ordenamientos y estadísticas
├── paises.csv              # Dataset base con los registros de países en formato CSV (UTF-8)
├── README.md               # Documentación general e instrucciones de uso del repositorio
└── documentacion_tpi.pdf   # Informe académico y técnico completo en formato PDF
```

---

## Funcionalidades del Sistema

El menú principal en consola ofrece las siguientes operaciones:

1. **Listar todos los países:** Muestra el catálogo completo en una tabla formateada con columnas alineadas y separadores de miles.
2. **Agregar un país:** Permite incorporar un nuevo país validando que ningún campo quede vacío, que población y superficie sean enteros positivos, que el continente sea válido (`América`, `Europa`, `Asia`, `África`, `Oceanía`) y que no existan nombres duplicados. Guarda el cambio automáticamente en `paises.csv`.
3. **Actualizar población y superficie de un país:** Localiza un país existente por nombre (insensible a mayúsculas y tildes), exhibe sus datos actuales, valida los nuevos valores numéricos y actualiza el archivo CSV.
4. **Buscar país por nombre:** Soporta búsqueda por **coincidencia parcial** o **coincidencia exacta**, ignorando tildes y diferencias entre mayúsculas y minúsculas.
5. **Filtrar países:**
   * Por continente.
   * Por rango de población (`mínimo` y `máximo`).
   * Por rango de superficie en $\text{km}^2$ (`mínimo` y `máximo`).
6. **Ordenar países:** Reorganiza una vista de los registros en sentido **ascendente** o **descendente** según:
   * Nombre (orden alfabético normalizado).
   * Población.
   * Superficie ($\text{km}^2$).
7. **Mostrar estadísticas:** Calcula e informa:
   * Total de países registrados.
   * País con mayor población y país con menor población.
   * Promedio general de población.
   * Promedio general de superficie ($\text{km}^2$).
   * Cantidad de países agrupados por continente.
0. **Salir:** Finaliza la ejecución del programa de forma controlada.

---

## Requisitos e Instrucciones de Ejecución

* **Requisitos:** Python 3.10 o superior. No requiere instalar librerías externas; utiliza únicamente la biblioteca estándar (`csv`).
* **Ejecución:**

```bash
python main.py
```

### Formato del Archivo `paises.csv`

El dataset utiliza codificación `UTF-8` con encabezados `nombre,poblacion,superficie,continente`:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

---

## Ejemplos de Entrada y Salida en Consola

### Alta de un país con validación de errores

```text
--- AGREGAR PAÍS ---
Nombre del país: 
[Error] El campo no puede quedar vacío.
Nombre del país: Perú
Población: -500
[Error] El número ingresado está fuera del rango permitido.
Población: 33715471
Superficie (km²): 1285216
Continente (América, Europa, Asia, África, Oceanía): America
[Éxito] País 'Perú' agregado correctamente.
```

### Consulta de estadísticas generales (dataset base de 20 países)

```text
==========================================
         ESTADÍSTICAS GENERALES           
==========================================
Total de países          : 20
Mayor población          : China (1,411,750,000 hab.)
Menor población          : Nueva Zelanda (5,122,600 hab.)
Promedio de población    : 211,601,943.55 hab.
Promedio de superficie   : 2,578,606.30 km²

Cantidad de países por continente:
  - América   : 6
  - Asia      : 4
  - Europa    : 5
  - África    : 3
  - Oceanía   : 2
==========================================
```
