numeros = []
for c in range(1, 6):
    numeros.append(int(input(f'Digite o {c}° número: ')))
maior = max(numeros)
menor = min(numeros)
print(f'O maior número da lista é o {maior} e está na posição {numeros.index(maior) + 1}')
print(f'O menor número da lista é o {menor} e está na posição {numeros.index(menor) + 1}')