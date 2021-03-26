# Autor: Mailson Felipe
# Data: 26/03/2021

def quantosNumeros(digito):
    qtd = 0
    valor = 1

    while valor <= digito:
        valor *= 10
        qtd += 1
        
    print("Quantidade de digitos: "+str(qtd))


def main():
	digito = int(input("Digite um numero: "))
	quantosNumeros(digito)

if __name__ == "__main__":
   main()