from random import randint

class Enciptar:
	def __init__(self):
		self.alfabeto = [x for x in 'k8ocdn0m16jxbre7t39pwhsvqzau4fyigl53']

	def receberFrase(self):
		self.frase = str(input('Digite uma frase: ')).lower()
	
	def receberCifra(self):
		try:
			self.cifra = int(input('Digite o valor da cifra: '))
		except ValueError:
			print('Digite um número')
			self.receberCifra()

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def criptarFrase(self):
		for self.letra in self.letras:
			if self.letra not in ' ':
				if self.letra in self.alfabeto:
					if self.alfabeto.index(self.letra) + self.cifra >= 36:
						if self.cifra >= 36:
							self.index = (self.cifra + self.alfabeto.index(self.letra)) % 36
							self.letrasEmbaralhadas.append(self.alfabeto[self.index])
						else:
							self.index = self.alfabeto.index(self.letra) + self.cifra - 36
							self.letrasEmbaralhadas.append(self.alfabeto[self.index])
					else:
						self.letrasEmbaralhadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
				else:
					self.letrasEmbaralhadas.append(self.letra)
			else:
				self.letrasEmbaralhadas.append('±')

	def inserirIndice(self):
		if self.cifra > 36:
			self.cifra %= 36
		self.posicaoAleatoria = randint(0, len(self.letrasEmbaralhadas) - 1)
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria, f'ß{self.cifra}')
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria + 2, '¶')
		
	def juntarLista(self):
		self.letrasJuntas = ''.join(self.letrasEmbaralhadas)
		print(self.letrasJuntas)

	def main(self):
		self.receberFrase()
		self.receberCifra()
		self.criarLista()
		self.criptarFrase()
		self.inserirIndice()
		self.juntarLista()

iniciar = Enciptar()
iniciar.main()