jogador = dict()
gols = list()
time = list()
jogadores = dict()

while True:
    jogador['nome'] = str(input('Jogador: '))
    partidas = int(input('Partidas Jogadas: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Gols na partida {c}: ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogadores = jogador.copy()
    jogador.clear()
    gols.clear()
    resposta = str(input('Deseja continuar? ')).upper()
    if resposta == 'N':
        break

print(40 * '=')
print('Cod. ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print('\n', end='')

for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('\n', end='')

while True:
    dado = int(input('Mostrar dados de qual jogador? '))
    print(f'Levantamento do jogador {time[dado]["nome"]}')
    for c, d in enumerate(time[dado]['gols']):
        print(f'No jogo {c + 1} ele fez {d}')
    if dado == -1:
        break