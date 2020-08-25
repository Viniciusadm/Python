cidade = str(input('Em qual cidade você nasceu? ')).strip().upper().split()
resposta = cidade[0] == 'SANTO'
if resposta == True:
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')
