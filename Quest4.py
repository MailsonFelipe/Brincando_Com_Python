from operator import itemgetter

# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	pessoas = [[] for _ in range(5)]

	for i in range(5):
		nome = input("Nome: ")
		idade = input("Idade: ")
		altura = input("Altura: ")

		pessoas[i].append(nome)
		pessoas[i].append(idade)
		pessoas[i].append(altura)

	pessoas = sorted(pessoas, key=itemgetter(1))

	print('\n')

	for x in range(5):
		print('Nome: '+str(pessoas[x][0]));
		print('Idade: '+str(pessoas[x][1]));
		if(pessoas[x][1] < 18):
			print('menor de idade')
		print('\n')

if __name__ == "__main__":
   main()
