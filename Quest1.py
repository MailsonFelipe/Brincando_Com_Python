# Autor: Mailson Felipe
# Data: 26/03/2021

def calculaNotas(nota1, nota2):
	if((nota1+nota2)/2 >= 10):
		print ("Aprovado com distincao.")
	elif((nota1+nota2)/2 >= 7):
		print("Aprovado")
	else:
		print("Reprovado")


def main():
	calculaNotas(10, 10)
	calculaNotas(7, 7)
	calculaNotas(1, 1)


if __name__ == "__main__":
   main()
