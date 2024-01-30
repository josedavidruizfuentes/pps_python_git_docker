def frotar(n_frases: int = 1) -> list():
    with open('frases.txt', 'r') as f:
        frases = [frase.strip() for frase in f.readlines()]
    return frases[:n_frases]
