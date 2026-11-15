from datos_csv import cargar_paises_csv, guardar_paises_csv
from gestor_paises import (
    CONTINENTES_VALIDOS,
    actualizar_pais,
    agregar_pais,
    buscar_indice_pais,
    buscar_paises,
    calcular_promedio_poblacion,
    calcular_promedio_superficie,
    contar_paises_por_continente,
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie,
    normalizar_continente,
    obtener_pais_mayor_poblacion,
    obtener_pais_menor_poblacion,
    ordenar_paises
)

RUTA_CSV = "paises.csv"


def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("[Error] El campo no puede quedar vacío.")


def leer_entero_positivo(mensaje, permitir_cero):
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
            if permitir_cero and numero >= 0:
                return numero
            if not permitir_cero and numero > 0:
                return numero
            print("[Error] El número ingresado está fuera del rango permitido.")
        except ValueError:
            print("[Error] Debe ingresar un número entero válido.")


def leer_rango_enteros(nombre_dato):
    while True:
        minimo = leer_entero_positivo(f"Ingrese {nombre_dato} mínima: ", True)
        maximo = leer_entero_positivo(f"Ingrese {nombre_dato} máxima: ", True)
        if minimo <= maximo:
            return minimo, maximo
        print("[Error] El valor mínimo no puede ser mayor al máximo.")


def leer_continente():
    while True:
        entrada = leer_texto_no_vacio("Continente (América, Europa, Asia, África, Oceanía): ")
        continente = normalizar_continente(entrada)
        if continente != "":
            return continente
        print("[Error] Continente inválido. Opciones:", ", ".join(CONTINENTES_VALIDOS))


def leer_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print("[Error] Opción incorrecta. Intente nuevamente.")


def mostrar_tabla_paises(paises, titulo):
    if len(paises) == 0:
        print("\n[Aviso] No se encontraron países para mostrar.")
        return

    print(f"\n=== {titulo} ({len(paises)} registros) ===")
    print("-" * 74)
    print(f"{'Nombre':<22} | {'Población':>15} | {'Superficie (km²)':>18} | {'Continente':<10}")
    print("-" * 74)
    for pais in paises:
        print(
            f"{pais['nombre']:<22} | "
            f"{pais['poblacion']:>15,} | "
            f"{pais['superficie']:>18,} | "
            f"{pais['continente']:<10}"
        )
    print("-" * 74)


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("\n[Aviso] No hay datos cargados para calcular estadísticas.")
        return

    mayor = obtener_pais_mayor_poblacion(paises)
    menor = obtener_pais_menor_poblacion(paises)
    prom_poblacion = calcular_promedio_poblacion(paises)
    prom_superficie = calcular_promedio_superficie(paises)
    por_continente = contar_paises_por_continente(paises)

    print("\n==========================================")
    print("         ESTADÍSTICAS GENERALES           ")
    print("==========================================")
    print(f"Total de países          : {len(paises)}")
    print(f"Mayor población          : {mayor['nombre']} ({mayor['poblacion']:,} hab.)")
    print(f"Menor población          : {menor['nombre']} ({menor['poblacion']:,} hab.)")
    print(f"Promedio de población    : {prom_poblacion:,.2f} hab.")
    print(f"Promedio de superficie   : {prom_superficie:,.2f} km²")
    print("\nCantidad de países por continente:")
    for continente, cantidad in por_continente.items():
        print(f"  - {continente:<10}: {cantidad}")
    print("==========================================")


def flujo_agregar_pais(paises):
    print("\n--- AGREGAR PAÍS ---")
    nombre = leer_texto_no_vacio("Nombre del país: ")
    poblacion = leer_entero_positivo("Población: ", False)
    superficie = leer_entero_positivo("Superficie (km²): ", False)
    continente = leer_continente()

    if agregar_pais(paises, nombre, poblacion, superficie, continente):
        guardar_paises_csv(RUTA_CSV, paises)
        print(f"[Éxito] País '{nombre.strip()}' agregado correctamente.")
    else:
        print(f"[Error] Ya existe un país registrado llamado '{nombre}'.")


def flujo_actualizar_pais(paises):
    print("\n--- ACTUALIZAR PAÍS ---")
    if len(paises) == 0:
        print("[Aviso] No hay países registrados.")
        return

    nombre = leer_texto_no_vacio("Ingrese el nombre exacto del país a actualizar: ")
    indice = buscar_indice_pais(paises, nombre)
    if indice == -1:
        print(f"[Error] No se encontró el país '{nombre}'.")
        return

    pais_actual = paises[indice]
    print(f"Actual: {pais_actual['nombre']} | Población: {pais_actual['poblacion']:,} | Superficie: {pais_actual['superficie']:,} km²")
    nueva_poblacion = leer_entero_positivo("Nueva población: ", False)
    nueva_superficie = leer_entero_positivo("Nueva superficie (km²): ", False)

    if actualizar_pais(paises, pais_actual["nombre"], nueva_poblacion, nueva_superficie):
        guardar_paises_csv(RUTA_CSV, paises)
        print(f"[Éxito] Datos de '{pais_actual['nombre']}' actualizados.")


def flujo_buscar_pais(paises):
    print("\n--- BUSCAR PAÍS ---")
    print("1. Coincidencia parcial")
    print("2. Coincidencia exacta")
    tipo = leer_opcion("Seleccione tipo de búsqueda (1-2): ", ["1", "2"])
    termino = leer_texto_no_vacio("Ingrese nombre o texto a buscar: ")

    es_exacta = tipo == "2"
    resultados = buscar_paises(paises, termino, es_exacta)
    mostrar_tabla_paises(resultados, f"RESULTADOS DE BÚSQUEDA ('{termino}')")


def flujo_filtrar_paises(paises):
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = leer_opcion("Seleccione filtro (1-3): ", ["1", "2", "3"])

    if opcion == "1":
        continente = leer_continente()
        resultados = filtrar_por_continente(paises, continente)
        mostrar_tabla_paises(resultados, f"PAÍSES DE {continente.upper()}")
    elif opcion == "2":
        minimo, maximo = leer_rango_enteros("población")
        resultados = filtrar_por_rango_poblacion(paises, minimo, maximo)
        mostrar_tabla_paises(resultados, f"POBLACIÓN ENTRE {minimo:,} Y {maximo:,}")
    elif opcion == "3":
        minimo, maximo = leer_rango_enteros("superficie (km²)")
        resultados = filtrar_por_rango_superficie(paises, minimo, maximo)
        mostrar_tabla_paises(resultados, f"SUPERFICIE ENTRE {minimo:,} Y {maximo:,} KM²")


def flujo_ordenar_paises(paises):
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    criterio_opcion = leer_opcion("Seleccione criterio (1-3): ", ["1", "2", "3"])

    print("1. Ascendente")
    print("2. Descendente")
    orden_opcion = leer_opcion("Seleccione orden (1-2): ", ["1", "2"])

    criterio = "nombre"
    if criterio_opcion == "2":
        criterio = "poblacion"
    elif criterio_opcion == "3":
        criterio = "superficie"

    descendente = orden_opcion == "2"
    ordenados = ordenar_paises(paises, criterio, descendente)
    mostrar_tabla_paises(ordenados, f"PAÍSES ORDENADOS POR {criterio.upper()}")


def mostrar_menu():
    print("\n====================================================")
    print("   GESTIÓN DE DATOS DE PAÍSES - PROGRAMACIÓN 1      ")
    print("====================================================")
    print("1. Listar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie de un país")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("0. Salir")
    print("====================================================")


def main():
    paises = cargar_paises_csv(RUTA_CSV)
    print(f"[Info] Se cargaron {len(paises)} países desde '{RUTA_CSV}'.")

    while True:
        mostrar_menu()
        opcion = leer_opcion("Seleccione una opción: ", ["0", "1", "2", "3", "4", "5", "6", "7"])

        match opcion:
            case "1":
                mostrar_tabla_paises(paises, "LISTADO COMPLETO DE PAÍSES")
            case "2":
                flujo_agregar_pais(paises)
            case "3":
                flujo_actualizar_pais(paises)
            case "4":
                flujo_buscar_pais(paises)
            case "5":
                flujo_filtrar_paises(paises)
            case "6":
                flujo_ordenar_paises(paises)
            case "7":
                mostrar_estadisticas(paises)
            case "0":
                print("\nPrograma finalizado. ¡Hasta luego!")
                break
            case _:
                print("[Error] Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()