print("Calculo de IMC")
peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))

imc = peso/(altura*altura)

if imc < 18.5:
  print("Você esta abaixo do peso")
elif imc < 25:
  print("Você esta com o peso ideal")
elif imc < 30:
  print("Você esta com sobre peso")
elif imc < 40:
  print("Você esta com obesidade")
elif 40 < imc:
  print("Você esta com obesidade morbida")