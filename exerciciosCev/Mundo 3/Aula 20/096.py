def caucularArea(largura, comprimento):
    area = float(larguraInput * comprimentoInput)
    print(f'A área de um terreno {largura}x{comprimento} é {area}m2')

print('Caucular área de um terreno')
larguraInput = float(input('Largura: '))
comprimentoInput = float(input('Comprimento: '))
caucularArea(larguraInput, comprimentoInput)