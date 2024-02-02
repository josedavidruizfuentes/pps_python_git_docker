from prueba_mongo import consulta

def frotar(n_frases: int = 1) -> list:
    frases_aleatorias = consulta(n_frases)
    return frases_aleatorias
