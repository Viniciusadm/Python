#Strings
frase = 'Olá, Mundo!'

len(frase)
', '.join(frase)
frase.strip()
frase.title()
frase.split()
frase.capitalize()
frase.upper()
frase.lower()
frase.replace('Olá', 'Oi')
frase.count('o')
frase.find('o')
frase.swapcase()
frase.rjust(10)
frase.ljust(10)
frase.center(10)

#Listas
lista = ['Laranja', 'tomate', 'feijão', 'batata']
listaNumeros = [1, 3, 5, 7]
listComprehensions = [valor ** 2 for valor in range(1,11)]

lista.append('arroz')
lista.insert(0, 'macarrão')
lista.index('Laranja')
del lista[1]
lista.pop(0)
lista.remove('batata')
lista.sort(reverse = True)
sorted(lista)
lista.reverse()
sum(listaNumeros)
min(listaNumeros)
max(listaNumeros)
