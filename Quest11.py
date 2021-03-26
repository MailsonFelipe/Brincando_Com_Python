import sys

# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	padrao = input("Insira a string padrao (DDMMM:HHmm): ")


	flag = 0
	dia = padrao[0]+padrao[1]
	mes = padrao[2]+padrao[3]+padrao[4]
	hora = padrao[06]+padrao[7]
	minutos = padrao[8]+padrao[9]

	if(len(dia) == 2):
		flag = 0;
	else:
		flag = 1
		print('False')
		sys.exit()

	if(len(mes) == 3 and (mes == 'JAN' or mes == 'FEV' or mes == 'MAR' or mes == 'APR' or mes == 'MAY' or mes == 'JUN' or mes == 'JUL' or mes == 'AUG'or mes == 'SEP' or mes == 'OCT'or mes == 'NOV' or mes == 'DEC')):
		flag = 0
	else:
		flag = 1;
		print('False')
		sys.exit()

	if (padrao[5] == ':'):
		flag = 0
	else:
		flag = 1
		print('False')
		sys.exit()

	if(len(hora) == 2):
		flag = 0
	else:
		flag = 1
		print('False')
		sys.exit()

	if (len(minutos) == 2):
		flag = 0
	else:
		flag = 1
		print('False')
		sys.exit()


	print('True')
		

if __name__ == "__main__":
   main()
