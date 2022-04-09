valores = []

for cont in range(0, 5):
  valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
  print(f"Na posição {c+1} eu encontrei o valor {v}")