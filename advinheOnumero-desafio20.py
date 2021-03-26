import random

print("Tente advinhar em qual numero entre 0 a 10 o computador esta pensando")

cont = 0

num = int(input("Digite um numero: "))

pcnum = random.randint(0, 10)

while num != pcnum:
  num = int(input("Digite outro numero: "))
  cont += 1

print("Você advinhou o numero depois de {} tentativas".format(cont)) 