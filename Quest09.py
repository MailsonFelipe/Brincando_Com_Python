# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	nome = input("Digite um nome: ")
	nome = nome.upper()

	for i in range(0, len(nome)+1):
		print(nome[:i])

if __name__ == "__main__":
   main()