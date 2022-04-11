num = (int(input("Digite um número: ")),
      int(input("Digite outro número: ")),
      int(input("Digite outro número: ")),
      int(input("Digite outro número: ")))

cont = 0

print(f"Você digitou os valores {num}")
print(f"O valor nove apareceu {num.count(9)} vezes")

for c in range(0, 4):
  if num[c] == 3:
    print(f"O valor 3 apareceu na posição {num.index(3)+1}")
  else:
    cont += 1

    if cont == 4:
      print(f"O valor 3 não foi digitado")

print("Os valores pares digitados foram: ")
for c in range(0, 4):
  if num[c] % 2 == 0:
    print(f" {num[c]}")