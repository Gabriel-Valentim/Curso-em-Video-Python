print("Soma todos os pares digitados")

s = 0

for soma in range(0, 6):
  n = int(input("Digite um numero: "))
  if n%2 == 0:
    s += n

print("Soma de todos os pares digitados: {}".format(s))
  