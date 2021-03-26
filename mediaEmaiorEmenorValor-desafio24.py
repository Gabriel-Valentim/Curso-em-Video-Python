continuar = 1
cont = 0
soma = 0

while continuar != 2:
  num = int(input("Digite um numero: "))
  soma += num

  if cont == 0:
    maior = num
    menor = num
  elif num > maior:
    maior = num
  elif num < menor:
    menor = num

  cont += 1

  continuar = int(input("Quer continuar digite 1 para sim e 2 para não: "))

media = soma/cont

print(f"A media dos numeros é {media} e o maior é {maior} e o menor é {menor}")