def frotar(n_frases: int = 1) -> list():
<<<<<<< HEAD
    frases = []
    for i in range(n_frases):
        frases.append("¡Hola, mundo!")
    return frases

=======
    with open('frases.txt', 'r') as f:
        frases = [frase.strip() for frase in f.readlines()]
    return frases[:n_frases]
>>>>>>> python
