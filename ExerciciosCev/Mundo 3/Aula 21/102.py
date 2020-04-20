def fatorial(numero, show=False):
    resultado = 1
    for c in range(numero, 0, -1):
        resultado *= c
    if show == True:
        for c, d in enumerate(range(numero, 0, -1)):
            if c + 1 != len(range(numero, 0, -1)):
                print(d, end=' * ')
            else:
                print(d, end=' = ')
    return resultado

print(fatorial(3, True))