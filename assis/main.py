import requests
from os import system

#print('''Menu
#01- Animes
#02- Log''')

#option = int(input(':'))
option = 1

system('clear')

if option == 1:
    req = requests.post("http://viniciusadm.000webhostapp.com/assis/api/python.php", data={'id_user' : '1'})
    req_json = req.json()
    tot = 0

    for c in req_json:
        faltam = int(c['ep_tot']) - int(c['ep_atual'])
        nome = c['nome']
        if c['status'] == '1' and faltam != 0:
            print(f'\033[1;31m{nome}\033[0;0m')
            print('Atual: ', end='')
            print(c['ep_atual'], end=' ')
            print('Total: ', end='')
            print(c['ep_tot'])
            print('Faltam', end=' ')
            print(f'\033[1;34m{faltam}\033[0;0m')
            tot += faltam

    print(tot)

elif option == 2:
    req = requests.post("http://viniciusadm.000webhostapp.com/assis/api/log.php", data={'id_user' : '1'})
    req_json = req.json()

    for log in req_json:
        occurrence = log['occurrence']
        date = log['date']
        date = date.split('-')
        date.reverse()
        date = '-'.join(date)
        print(occurrence)
        print(f'Data: {date}')
