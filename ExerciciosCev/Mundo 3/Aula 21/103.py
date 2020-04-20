def ficha(jogador = '<desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campenato')

nome = str(input('Nome do jogador: '))
golsNumero = str(input('Gols: '))

if golsNumero.isnumeric():
    golsNumero = int(golsNumero)
else:
    golsNumero = 0

if nome.strip() == '':
    ficha(gols=golsNumero)
else:
    ficha(nome, golsNumero)