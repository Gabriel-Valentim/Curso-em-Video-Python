cont = 0

exp = str(input("Digite uma expressão: "))

for c in exp:
  if c == '(' or c == ')':
    cont += 1

if cont % 2 == 0:
  print("Expressão valida")
else:
  print("Expressão invalida")
  