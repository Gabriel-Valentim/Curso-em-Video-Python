pessoas = []
dados = []
cont = 0
maior = menor = 0
continuar = 'S'

while True:
  pessoas.append(str (input(f"Nome: ")))
  pessoas.append(int(input(f"Peso: ")))

  dados.append(pessoas[:])

  if cont == 0:
    maior = pessoas[1]
    menor = pessoas[1]
  else:
    if pessoas[1] > maior:
      maior = pessoas[1]
    elif pessoas[1] < menor:
      menor = pessoas[1]

  pessoas.clear()

  continuar = input(str("Quer continuar[S/N]: "))
  cont += 1
  if continuar == 'N':
    break

print(f"Foram cadastradas {cont} pessoas")
print(f"O maior peso foi {maior}. De ", end="")
for p in dados:
  if p[1] == maior:
    print(f"{p[0]} ", end="")
print(f"\nO menor peso foi {menor}. De ", end="")
for p in dados:
  if p[1] == menor:
    print(f"{p[0]} ", end="")