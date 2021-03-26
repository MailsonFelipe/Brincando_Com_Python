import csv
# Autor: Mailson Felipe
# Data: 26/03/2021


# Assumindo que o csv esta no formato [idade, altura]
file =  open('alunos.csv', 'r')
reader = csv.reader(file)

itens =[] 
idade = []
altura = []

for linha in reader:
	itens.append(linha)

for i in range (1, len(itens)):
	idade.append(itens[i][0])
	altura.append(itens[i][1])

idade = [int(i) for i in idade]
altura = [float(i) for i in altura]

mediaAltura = sum(altura)/len(altura)
print('Media: '+str(mediaAltura))
qtd_alunos = 0

for i in range(len(idade)):
	if (idade[i] > 13 and altura[i] < mediaAltura):
		qtd_alunos += 1


print(str(qtd_alunos)+' alunos')



# Caso de teste usado:

'''
idade, altura
15, 1.80
20, 1.86
18, 1.67
19, 2.00
17, 1.58
13, 1.69
14, 1.88
18, 1.76
17, 1.89
19, 1.67
'''