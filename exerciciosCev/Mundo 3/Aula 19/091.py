from random import randint
from time import sleep
from operator import itemgetter

ranking = 'Ranking'
jogadas = dict()
jogadasOrdenadas = dict()

for c in range(1, 5):
    jogadas[f'Jogador{c}'] = randint(1, 6)

for c, d in jogadas.items():
    print(f'O {c} tirou {d}')
    sleep(0.6)

jogadasOrdenadas = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(f'{ranking:-^31}')
for c, d in enumerate(jogadasOrdenadas):
    print(f'{c + 1}° lugar: {d[0]} que tirou {d[1]}')
    sleep(0.6)