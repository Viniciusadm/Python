def escreva(palavra):
    tamanho = len(palavra) + 4
    print(tamanho * '~')
    print(f'  {palavra}')
    print(tamanho * '~')

string = input('Qual palavra você deseja escrever? ')
escreva(string)