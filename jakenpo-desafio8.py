import random

print("Jakenpo com o computado")
jakenpo = str(input("Oque você vai escolher: "))
computador = random.randint(1,3)

if computador == 1:
  computador = "pedra"
  if computador == "pedra" and jakenpo == "papel":
    print("Você ganhou, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  elif computador == "pedra" and jakenpo == "tesoura":
    print("Você perdeu, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  else:
    print("Empate, pois ambos escolheram {}".format(computador))

elif computador == 2:
  computador = "papel"
  if computador == "papel" and jakenpo == "pedra":
    print("Você perdeu, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  elif computador == "papel" and jakenpo == "tesoura":
    print("Você ganhou, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  else:
    print("Empate, pois ambos escolheram {}".format(computador))

else:
  computador = "tesoura"
  if computador == "tesoura" and jakenpo == "pedra":
    print("Você ganhou, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  elif computador == "tesoura" and jakenpo == "papel":
    print("Você perdeu, pois você escolheu {} e o computador {}".format(jakenpo, computador))
  else:
    print("Empate, pois ambos escolheram {}".format(computador))