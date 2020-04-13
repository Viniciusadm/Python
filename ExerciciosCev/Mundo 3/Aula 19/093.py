jogador = dict()
gols = []

jogador['Nome'] = str(input('Jogador: '))
partidas = int(input('Partidas Jogadas: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Gols na partida {c}: ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)

print(40 * '=')

for c, d in jogador.items():
    print(f'O campo {c} tem o valor {d}.')

print(40 * '=')

print('O jogador', jogador['Nome'], f'jogou {partidas} partidas.')
for c, d in enumerate(gols):
    print(f'Na partida {c + 1}, fez {d} gols')