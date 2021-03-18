print("Soma de todos os impares multiplos de 3")

s = 0

for soma in range(1, 500, 2):
  aux = soma
  if aux%3 == 0:
    s += soma

print("A soma deu: {}".format(s))