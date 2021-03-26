import zeep

wsdl = 'https://www.dataaccess.com/webservicesserver/numberconversion.wso?op=NumberToDollars'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))

#QUESTAO INCOMPLETA

def main():

	option = 0

	while(True):
		print('Aperte:')
		print('1. Para conversao de numeros')
		print('2. Para Number to Dollar')
		print('3. Para sair')
		input('Escolha: ')
		if(option == 3):
			break

if __name__ == "__main__":
   main()
