from random import shuffle

alfabeto = [x for x in '0123456789abcdefghijklmnopqrstuvwxyz']
embaralhado = ['k', '8', 'o', 'c', 'd', 'n', '0', 'm', '1', '6', 'j', 'x', 'b', 'r', 'e', '7', 't', '2', '9', 'p', 'w', 'h', 's', 'v', 'q', 'z', 'a', 'u', '4', 'f', 'y', 'i', 'g', 'l', '5', '3']
shuffle(alfabeto)

print(''.join(embaralhado))
