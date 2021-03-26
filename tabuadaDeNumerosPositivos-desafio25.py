num = int(input("Digite um numero: "))
cont = 0

while num > -1:
  cont += 1
  tab = cont*num

  print(f"{num} X {cont} : {tab}")

  if cont == 10:
    cont = 0 
    num = int(input("Digite um numero: "))

print("acabou")