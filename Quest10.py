# Autor: Mailson Felipe
# Data: 26/03/2021

class Carro(object):
	"""docstring for Carro"""
	def __init__(self, gasto):
		self.gasto = gasto
		self.combustivel = 0

	def andar(self, distancia):
		gasto = self.gasto * distancia
		self.combustivel -= gasto

	def obterGasolina(self):
		return self.combustivel

	def adicionarGasolina(self, combustivel):
		self.combustivel += combustivel




def main():
	meuFusca = Carro(15);
	meuFusca.adicionarGasolina(20);
	meuFusca.andar(100);
	print(meuFusca.obterGasolina())	

if __name__ == "__main__":
   main()