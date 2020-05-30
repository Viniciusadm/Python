class CifraCesar:
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

	def criptarFrase(self):
		for self.letra in self.frase:
			if self.letra in self.alfabeto:
				if self.alfabeto.index(self.letra) + self.cifra >= 36:
					if self.cifra >= 36:
						self.index = (self.cifra + self.alfabeto.index(self.letra)) % 36
						print(self.alfabeto[self.index], end='')
					else:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 36
						print(self.alfabeto[self.index], end='')
				else:
					print(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra], end='')
			else:
				print(self.letra, end='')
		print('')

	def main(self):
		self.receberFrase()
		self.receberCifra()
		self.criptarFrase()

iniciar = CifraCesar()
iniciar.main()