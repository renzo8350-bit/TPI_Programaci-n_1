# Gestión de Datos de Países en Python: Filtros, Ordenamientos y Estadísticas

**Trabajo Práctico Integrador (TPI) — Programación 1**  
**Universidad Tecnológica Nacional (UTN)** · *Tecnicatura Universitaria en Programación a Distancia*  
**Estudiante:** Pazquier Renzo · **Comisión:** 3 · **Docente:** Cintia Rigoni

---

## 1. Descripción del Programa

Esta aplicación de consola desarrollada en **Python 3** permite gestionar, consultar y analizar un catálogo de países almacenado en formato CSV (`paises.csv`). El sistema modela cada país como un diccionario con los atributos `nombre`, `poblacion`, `superficie` (en km²) y `continente` dentro de una lista principal en memoria, aplicando programación modular, validación defensiva de entradas y persistencia automática.

### Funcionalidades principales
- **Carga y validación CSV**: Lectura segura desde `paises.csv` con control de encabezados, tipos numéricos y filas malformadas.
- **Alta de países**: Registro de nuevos países verificando campos no vacíos, enteros positivos y ausencia de duplicados, con guardado automático en CSV.
- **Actualización de datos**: Modificación de población y superficie de un país existente con persistencia inmediata.
- **Búsqueda por nombre**: Consulta insensible a mayúsculas y tildes por coincidencia **parcial** o **exacta**.
- **Filtrado multicriterio**:
  - Por continente.
  - Por rango de población (`mínimo` – `máximo`).
  - Por rango de superficie en km² (`mínimo` – `máximo`).
- **Ordenamiento**: Clasificación ascendente o descendente por **nombre**, **población** o **superficie**.
- **Estadísticas descriptivas**: País con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.

---

## 2. Estructura del Proyecto

```text
tpi-gestion-paises-python/
├── main.py                  # Interfaz de consola, menú principal y validación de entradas
├── gestor_paises.py         # Lógica de negocio: altas, actualizaciones, filtros, ordenamientos y estadísticas
├── datos_csv.py             # Lectura, validación estructural y guardado del archivo CSV
├── paises.csv               # Dataset base con 20 países de los 5 continentes
├── README.md                # Documentación general y guía de ejecución
└── documentacion_tpi.pdf    # Informe académico y técnico completo del proyecto
```

---

## 3. Requisitos e Instrucciones de Uso

1. **Requisitos**: Tener instalado **Python 3.10 o superior**. El proyecto utiliza exclusivamente módulos de la biblioteca estándar (`csv`, `os`, `unicodedata`), por lo que no requiere instalar paquetes externos.
2. **Clonar o descargar el repositorio**:
   ```bash
   git clone https://github.com/usuario/tpi-gestion-paises-python.git
   cd tpi-gestion-paises-python
   ```
3. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```
   *(En sistemas Linux/macOS puede requerirse `python3 main.py`).*

---

## 4. Ejemplos de Entradas y Salidas

### Ejemplo 1: Inicio y Menú Principal
```text
[INFO] Se cargaron 20 países desde 'paises.csv'.

======================================================
  SISTEMA DE GESTIÓN DE DATOS DE PAÍSES (UTN - TPI)
======================================================
1. Listar todos los países
2. Agregar un nuevo país
3. Actualizar población y superficie de un país
4. Buscar país por nombre (parcial o exacta)
5. Filtrar países (continente / población / superficie)
6. Ordenar países (nombre / población / superficie)
7. Mostrar estadísticas generales
0. Salir del programa
======================================================
Ingrese una opción: 4
```

### Ejemplo 2: Búsqueda Parcial por Nombre
```text
=== BUSCAR PAÍS POR NOMBRE ===
Tipo de búsqueda: [1] Coincidencia parcial  |  [2] Coincidencia exacta
Seleccione una opción (1 o 2): 1
Ingrese el nombre o fragmento a buscar: argen

--- RESULTADOS DE BÚSQUEDA PARCIAL: 'argen' (1 registro/s) ---
--------------------------------------------------------------------------------
PAÍS                   | CONTINENTE     |   POBLACIÓN (hab.) |   SUPERFICIE (km²)
--------------------------------------------------------------------------------
Argentina              | América        |         45.376.763 |          2.780.400
--------------------------------------------------------------------------------
```

### Ejemplo 3: Estadísticas Generales (Opción 7)
```text
=== ESTADÍSTICAS DEL DATASET ===
Total de países registrados : 20
País con mayor población    : China (1.411.750.000 hab.)
País con menor población    : Nueva Zelanda (5.122.600 hab.)
Promedio de población       : 205.870.958,65 hab.
Promedio de superficie      : 2.666.526,30 km²

Cantidad de países por continente:
  - África         : 3 país/es
  - América        : 6 país/es
  - Asia           : 5 país/es
  - Europa         : 5 país/es
  - Oceanía        : 2 país/es
```

### Ejemplo 4: Validación ante Entrada Inválida
```text
=== AGREGAR NUEVO PAÍS ===
Nombre del país: 
[ERROR] El campo no puede quedar vacío. Intente nuevamente.
Nombre del país: Perú
Población (habitantes): -500
[ERROR] El valor debe ser mayor o igual a 1.
```

---

## 5. Autoría y Desarrollo Individual

| Estudiante | Comisión | Alcance del Desarrollo |
| :--- | :--- | :--- |
| **Pazquier Renzo** | Comisión 3 (Docente: Cintia Rigoni) | Diseño e implementación integral del sistema: persistencia y validación CSV (`datos_csv.py`), lógica de búsquedas, filtros, ordenamientos y estadísticas (`gestor_paises.py`), interfaz de consola (`main.py`), dataset (`paises.csv`) y documentación académica. |

---

## 6. Enlaces Obligatorios de Entrega

- **Documentación Académica y Técnica (PDF)**: Disponible en la raíz del repositorio como `documentacion_tpi.pdf` (o en el enlace: `[Insertar enlace público al PDF]`).
- **Video Demostrativo (10–15 min)**: `[Insertar enlace público al video demostrativo]`# TPI_Programaci-n_1
