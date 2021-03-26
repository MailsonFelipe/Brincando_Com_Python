import re

# Autor: Mailson Felipe
# Data: 26/03/2021

def main():
	frase = input("Digite uma string: ")
	print(re.sub(r'[^a-zA-Z0-9 ]',r'',frase))

if __name__ == "__main__":
   main()