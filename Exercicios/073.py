times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo',	'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco')
timesAlfabetico = sorted(times)

print('Os 5 primeiros colocados são: ')
print(15 * '-')
for contador in times[0 : 5]:
    print(f'|{contador:^13}|')
print(15 * '-')

print('\n')

print('Os ultimos 4 colocados da tabela são: ')
print(15 * '-')
for contador in times[-4:]:
    print(f'|{contador:^13}|')
print(15 * '-')

print('\n')

print('Os times em ordem alfabética são: ')

print(15 * '-')
for contador in timesAlfabetico:
        print(f'|{contador:^13}|')
print(15 * '-')

print('\n')

print(f' O time Botafogo está na posição {times.index("Botafogo") + 1}')