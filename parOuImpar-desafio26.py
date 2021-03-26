import random

cont = 0

print("Vamos jogar par ou impar")

num = int(input("Digite um numero: "))
escolha = str(input("Você quer par ou impar [P/I]: "))

pc = random.randint(1, 10)

if escolha == "P":
  pcEscolha = "I"
else:
  pcEscolha = "P"

soma = num + pc

if soma % 2 == 0 and escolha == "P":
  parImpar = True
  result = "PAR"
elif soma % 2 == 1 and escolha == "I":
  parImpar = True
  result = "IMPAR"
elif soma % 2 == 0 and pcEscolha == "P":
  parImpar = False
  result = "PAR"
else:
  parImpar = False
  result = "IMPAR"

print(f"Você jogou {num}, e o computador {pc}, a soma deu {soma} e deu {result}")

while parImpar == True:
  cont += 1

  num = int(input("Digite um numero: "))
  escolha = str(input("Você quer par ou impar [P/I]: "))

  pc = random.randint(1, 10)

  if escolha == "P":
    pcEscolha = "I"
  else:
    pcEscolha = "P"

  soma = num + pc

  if soma % 2 == 0 and escolha == "P":
    parImpar = True
  elif soma % 2 == 1 and escolha == "I":
    parImpar = True
  elif soma % 2 == 0 and pcEscolha == "P":
    parImpar = False
    result = "PAR"
  else:
    parImpar = False
    result = "IMPAR"

  print(f"Você jogou {num}, e o computador {pc}, a soma deu {soma} e deu {result}")

print(f"GAME OVER, você ganhou {cont} vezes")