formula = str(input('Digite a expressão: '))

parentesesEsquerdos = formula.count('(')
parentesesDireitos = formula.count(')')
parentesesEsquerdosPrimeiro = formula.find('(')
parentesesDireitosPrimeiro = formula.find(')')

if parentesesDireitos == parentesesEsquerdos and parentesesEsquerdosPrimeiro < parentesesDireitosPrimeiro:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')