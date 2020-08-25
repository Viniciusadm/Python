from os import system

def desempacotarLista(lista, separador):
    for c, d in enumerate(lista):
        if c + 1 != len(lista):
            print(d, end=separador)
        else:
            print(d)

def apagarTela():
    system('clear')
