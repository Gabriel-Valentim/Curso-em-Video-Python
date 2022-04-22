pri = []
par = []
impar = []
contP = 0

for c in range(0, 7):
  num = int(input(f"Digite o {c+1} valor: "))

  if num % 2 == 0:
    par.append(num)
    contP += 1
  else:
    impar.append(num)

par.sort()
impar.sort()

pri = par + impar 

print(f"Os valores pares digitados foram: ", end="")
for c in range(0, contP):
  print(f"{pri[c]} ", end='')

print(f"\nOs valores impares digitados foram: ", end="")
for c in range(contP, 7):
  print(f"{pri[c]} ", end='')