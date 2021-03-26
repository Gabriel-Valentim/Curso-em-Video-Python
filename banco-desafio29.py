nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

valor = int(input("Qual o valor que você quer sacar: "))

while True:

  if valor >= 50:

    if valor % 50 == 0:
      nota50 = valor/50
    else:
      resto50 = valor%50
      resto50 = valor - resto50
      nota50 = resto50/50

    valor = valor - (nota50*50)
    
    if valor == 0:
      break

  if valor >= 20:

    if valor % 20 == 0:
      nota20 = valor/20
    else:
      resto20 = valor%20
      resto20 = valor - resto20
      nota20 = resto20/20

    valor = valor - (nota20*20)
    
    if valor == 0:
      break

  if valor >= 10:

    if valor % 10 == 0:
      nota10 = valor/10
    else:
      resto10 = valor%10
      resto10 = valor - resto10
      nota10 = resto10/10

    valor = valor - (nota10*10)

    if valor == 0:
      break

  if valor >= 5:

    if valor % 5 == 0:
      nota5 = valor/5
    else:
      resto5 = valor%5
      resto5 = valor - resto5
      nota5 = resto5/5

    valor = valor - (nota5*5)
    
    if valor == 0:
      break
      
  if valor >= 1:

    nota5 = valor/1

    break

if nota50 != 0:
  print(f"Total de {nota50} notas de 50 reais")

if nota20 != 0:
  print(f"Total de {nota20} notas de 20 reais")

if nota10 != 0:
  print(f"Total de {nota10} notas de 10 reais")

if nota5 != 0:
  print(f"Total de {nota5} notas de 5 reais")

if nota1 != 0:
  print(f"Total de {nota1} notas de 1 reais")