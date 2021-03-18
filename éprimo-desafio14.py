print("Programa para ver se determinado numero é primo")

primo = int(input("Digite um numero: "))

cont = 0

for numeros in range(1, primo+1):
  if primo % numeros == 0:
    cont += 1

if cont == 2:
  print("O numero {} é primo".format(primo))
elif primo == 1 or primo == 2:
  print("O numero {} é primo".format(primo))
else:
  print("O numero {} não é primo".format(primo))