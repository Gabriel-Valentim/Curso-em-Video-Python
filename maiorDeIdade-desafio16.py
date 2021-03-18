print("Programa para ver quem ja atingiu a maioridade")

contMaior = 0
contMenor = 0

for i in range(0, 6):
  idade = int(input("Qual seu ano de nascimento: "))

  if 2021 - idade >= 21:
    contMaior += 1
  else:
    contMenor += 1

print("Das 6 pessoas, temos {} maiores de idade, e {} menores de idade".format(contMaior, contMenor))