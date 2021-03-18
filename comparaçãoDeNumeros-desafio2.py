num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num2 < num1:
  print("O primeiro valor é maior que o segundo")
elif num1 < num2:
  print("O segundo valor é maior que o primeiro")
else:
  print("Os numeros são iguais")