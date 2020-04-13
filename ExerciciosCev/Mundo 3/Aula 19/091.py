from random import randint
jogadas = dict()
jogadasOrdenadas = dict()

for c in range(1, 5):
    jogadas[f'Jogador{c}'] = randint(1, 6)

for c, d in enumerate(jogadas.values()):
    print(f'O Jogador {c + 1} tirou {d}')

