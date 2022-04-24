num = []
par = []
impar = []
continuar = 'S'

while True:
  num.append(int(input(f"Digite um numero: ")))

  continuar = input(str("Quer continuar[S/N]: "))

  if continuar == 'N':
    break

for c in range(0, len(num)):
  if num[c] % 2 == 0:
    par.append(num[c])
  else:
    impar.append(num[c])

print(f"Lista com todos os valores {num}")
print(f"Lista com apenas os valores pares {par}")
print(f"Lista com apenas os valores impares {impar}")