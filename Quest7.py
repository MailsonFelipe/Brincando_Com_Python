# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	data = input("Digite uma data no formato DD/MM/AAAA: ")
	dia = data.split('/')[0]
	mes = data.split('/')[1]
	ano = data.split('/')[2]
	
	auxDia = int(data.split('/')[0])
	auxMes = int(data.split('/')[1])

	if (auxDia < 1 or auxDia > 31):
		print('Dia invalido')
		return 0
	elif(len(ano) != 4):
		print('Ano invalido')
		return 0
	elif (auxMes < 1 and auxMes > 12):
		print('Mes invalido')
		return 0

	if(mes == 1):
		mes = 'Janeiro'
	elif(mes == 2):
		mes = 'Fevereiro'
	elif(mes == 3):
		mes = 'Marco'
	elif(mes == 4):
		mes = 'Abril'
	elif(mes == 5):
		mes = 'Maio'
	elif(mes == 6):
		mes = 'Junho'
	elif(mes == 7):
		mes = 'Julho'
	elif(mes == 8):
		mes = 'Agosto'
	elif(mes == 9):
		mes = 'Setembro'
	elif(mes == 10):
		mes = 'Outubro'
	elif(mes == 11):
		mes = 'Novembro'
	elif(mes == 12):
		mes = 'Dezembro'

	print('Data: '+dia+' de '+mes+ ' de '+ano)

if __name__ == "__main__":
   main()
   #'12/11/1212'