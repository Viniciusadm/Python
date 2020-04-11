total = contador = contadormil = menorPreco = 0
opcao = menorNome = ''
print('Compras')

while True:
    nome = str(input('Nome :'))
    preco = int(input('Preço: R$'))
    opcao = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    
    while contador != 1:
        contador += 1
        menorPreco = preco
        menorNome = nome

    total += preco

    if preco > 1000:
        contadormil =+ 1
    
    if preco < menorPreco:
        menorNome = nome
        menorPreco = preco

    if opcao == 'N':
        break

print(f'Total gasto na compra {total}')
print(f'Total de produtos que custam mais de R$1000: {contadormil}')
print(f'O produto mais barato é o {menorNome} e custa R${menorPreco}')