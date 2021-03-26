num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

op = 0

while op != 5:
  print("Menu digite a opção desejada")
  print("1 para somar os numeros digitados")
  print("2 para multiplicar os numeros digitados")
  print("3 para ver qual é o maior numero")
  print("4 para receber novos numeros")
  print("5 para sair sem fazer nada")

  op = int(input("Opção: "))

  if op == 1:
    soma = num1+num2
    print("A soma deles é {}".format(soma))

  elif op == 2:
    mult = num1*num2
    print("A multiplicação deles é {}".format(mult))

  elif op == 3:
    if num1 > num2:
      maior = num1
    else:
      maior = num2

    print("O maior numero é {}".format(maior))

  elif op == 4:
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))