# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	l = []
	aux = ''

	while (True):
		num = input('Digite um numero: ')
		if(num == -1):
			break
		else:
			l.append(num)	
	
	print('Quantidade de numeros: '+str(len(l)))
	
	for i in range(len(l)):
		aux += str(l[i])+' '
	print(aux)
	
	for i in range(len(l)):
		print(l[::-1][i])

	soma = sum(l)
	print('Soma: '+str(soma))

	media = sum(l) / len(l)
	print('Media: '+str(media))

	print('Valores acima da media:')
	for i in range(len(l)):
		if(l[i] > media):
			print(l[i])

	aux = 0;
	print('Valores abaixo de 7:')
	for i in range(len(l)):
		if(l[i] < 7):
			aux += 1
	print(aux)

if __name__ == "__main__":
   main()
