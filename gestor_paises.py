CONTINENTES_VALIDOS = ("América", "Europa", "Asia", "África", "Oceanía")


def normalizar_texto(texto):
    texto = texto.strip().lower()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    return texto


def normalizar_continente(continente):
    clave = normalizar_texto(continente)
    for valido in CONTINENTES_VALIDOS:
        if normalizar_texto(valido) == clave:
            return valido
    return ""


def buscar_indice_pais(paises, nombre):
    objetivo = normalizar_texto(nombre)
    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == objetivo:
            return i
    return -1


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    if buscar_indice_pais(paises, nombre) != -1:
        return False

    nuevo_pais = {
        "nombre": nombre.strip(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    return True


def actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie):
    indice = buscar_indice_pais(paises, nombre)
    if indice == -1:
        return False

    paises[indice]["poblacion"] = nueva_poblacion
    paises[indice]["superficie"] = nueva_superficie
    return True


def buscar_paises(paises, termino, coincidencia_exacta):
    resultados = []
    objetivo = normalizar_texto(termino)
    for pais in paises:
        nombre_pais = normalizar_texto(pais["nombre"])
        if coincidencia_exacta:
            if nombre_pais == objetivo:
                resultados.append(pais)
        else:
            if objetivo in nombre_pais:
                resultados.append(pais)
    return resultados


def filtrar_por_continente(paises, continente):
    resultados = []
    objetivo = normalizar_texto(continente)
    for pais in paises:
        if normalizar_texto(pais["continente"]) == objetivo:
            resultados.append(pais)
    return resultados


def filtrar_por_rango_poblacion(paises, minimo, maximo):
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    return resultados


def filtrar_por_rango_superficie(paises, minimo, maximo):
    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    return resultados


def obtener_nombre(pais):
    return normalizar_texto(pais["nombre"])


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


def ordenar_paises(paises, criterio, descendente):
    if criterio == "nombre":
        return sorted(paises, key=obtener_nombre, reverse=descendente)
    elif criterio == "poblacion":
        return sorted(paises, key=obtener_poblacion, reverse=descendente)
    elif criterio == "superficie":
        return sorted(paises, key=obtener_superficie, reverse=descendente)
    return paises


def obtener_pais_mayor_poblacion(paises):
    if len(paises) == 0:
        return None
    return max(paises, key=obtener_poblacion)


def obtener_pais_menor_poblacion(paises):
    if len(paises) == 0:
        return None
    return min(paises, key=obtener_poblacion)


def calcular_promedio_poblacion(paises):
    if len(paises) == 0:
        return 0.0
    suma = 0
    for pais in paises:
        suma += pais["poblacion"]
    return suma / len(paises)


def calcular_promedio_superficie(paises):
    if len(paises) == 0:
        return 0.0
    suma = 0
    for pais in paises:
        suma += pais["superficie"]
    return suma / len(paises)


def contar_paises_por_continente(paises):
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo