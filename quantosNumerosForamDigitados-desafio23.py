num = int(input("Digite um numero: "))

cont = 0
soma = 0

while num != 999:
  cont += 1
  soma = soma + num
  num = int(input("Digite um numero: "))

print("Foram digitados {} numeros e a soma deles é {}".format(cont, soma))