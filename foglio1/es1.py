def stampa(lista):
    print(lista)


def statistiche(lista):

    if not all(isinstance(n, int) for n in lista):
        return 'not integers'

    somma = sum(lista)
    media = sum(lista) / len(lista)
    minimo = min(lista)
    massimo = max(lista)

    return {
        'somma': somma,
        'media': media,
        'minimo': minimo,
        'massimo': massimo
    }


def somma_vettoriale(lista1, lista2):

    if not all(isinstance(n, int) for n in lista1 + lista2):
        return []

    if len(lista1) != len(lista2):
        return []
    
    return [a + b for a, b in zip(lista1, lista2)]


r = somma_vettoriale([1, 2, 3], [1, 2, 3])
print(r)
