# Autor: Mailson Felipe
# Data: 26/03/2021

def calculaAnos(a, b):

	anos = 0;

	while (a <= b):
		a += a * 0.03
		b += b * 0.015
		anos += 1

	print('Levarao '+ str(anos) + ' anos')


def main():
	a = 88167
	b = 199561

	calculaAnos(a, b)

if __name__ == "__main__":
   main()
