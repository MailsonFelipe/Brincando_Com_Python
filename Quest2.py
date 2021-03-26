# Autor: Mailson Felipe
# Data: 26/03/2021


def validaDados(nome, idade, salario, sexo, estadocivil):
	if(len(nome)>3 and idade>-1 and idade <151 and salario > 0 and (sexo=='f' or sexo=='m') and (estadocivil=='s'or estadocivil=='c' or estadocivil=='v' or estadocivil=='d')):
		print('dados lidos com sucesso')
		return True
	else:
		print ('algum dado incorreto')
		return False


def main():
	while True:
		nome = input('Nome: ')
		idade = input('Idade: ')
		salario = input('Salario: ')
		sexo = input('sexo: ')
		estadocivil = input('Estado Civil: ')

		if (validaDados(nome, idade, salario, sexo, estadocivil) == True):
			break


if __name__ == "__main__":
   main()
