print("A palavra é palindromo ?")

frase = input('Digite uma frase: ').strip()
frase = frase.replace(' ', '') 

aux = ""

for i in range(0, len(frase)):
	aux += frase[len(frase)-(1+i)]

if aux == frase: 
	print('A frase é palíndroma!!')
else:
	print('A frase não é palíndroma. ')