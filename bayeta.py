from prueba_mongo import insertar_datos, consulta

def insertar_frases(nuevas_frases):
    insertar_datos(nuevas_frases)

def frotar(n_frases: int = 1) -> list:
    frases_aleatorias = consulta(n_frases)
    return frases_aleatorias