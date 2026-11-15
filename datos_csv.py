import csv

ENCABEZADOS = ["nombre", "poblacion", "superficie", "continente"]
CONTINENTES_VALIDOS = ("América", "Europa", "Asia", "África", "Oceanía")


def normalizar_texto_basico(texto):
    texto = texto.strip().lower()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    return texto


def normalizar_continente_csv(continente):
    clave = normalizar_texto_basico(continente)
    for valido in CONTINENTES_VALIDOS:
        if normalizar_texto_basico(valido) == clave:
            return valido
    return ""


def validar_fila_pais(fila):
    nombre = str(fila.get("nombre", "")).strip()
    poblacion_texto = str(fila.get("poblacion", "")).strip()
    superficie_texto = str(fila.get("superficie", "")).strip()
    continente_texto = str(fila.get("continente", "")).strip()

    if nombre == "" or poblacion_texto == "" or superficie_texto == "" or continente_texto == "":
        return None

    try:
        poblacion = int(poblacion_texto)
        superficie = int(superficie_texto)
    except ValueError:
        return None

    if poblacion <= 0 or superficie <= 0:
        return None

    continente = normalizar_continente_csv(continente_texto)
    if continente == "":
        return None

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    return pais


def cargar_paises_csv(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames is None:
                print("[Error] El archivo CSV está vacío.")
                return paises

            encabezados_archivo = []
            for columna in lector.fieldnames:
                encabezados_archivo.append(columna.strip().lower())

            for obligatorio in ENCABEZADOS:
                if obligatorio not in encabezados_archivo:
                    print("[Error] El archivo CSV no tiene las columnas esperadas.")
                    return paises

            numero_fila = 2
            for fila in lector:
                pais = validar_fila_pais(fila)
                if pais is not None:
                    paises.append(pais)
                else:
                    print(f"[Aviso] Fila {numero_fila} ignorada por tener datos inválidos.")
                numero_fila += 1

    except FileNotFoundError:
        print(f"[Error] No se encontró el archivo '{ruta_archivo}'.")
    except OSError as error:
        print(f"[Error] No se pudo leer el archivo: {error}")

    return paises


def guardar_paises_csv(ruta_archivo, paises):
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        return True
    except OSError as error:
        print(f"[Error] No se pudo guardar el archivo: {error}")
        return False