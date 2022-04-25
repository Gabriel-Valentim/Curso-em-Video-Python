num = []
continuar = 'S'
cont = 0

while True:
  num.append(int(input(f"Digite um numero: ")))

  continuar = input(str("Quer continuar[S/N]: "))

  cont += 1

  if continuar == 'N':
    break

num.sort(reverse=True)

tem = 0 

for c in num:
  if c == 5:
    tem = 1
    print("O valor 5 foi digitado na lista")

if tem == 0:
  print("O valor 5 não foi digitado na lista")

print(f"Foram digitados {cont} numeros")

print(num)