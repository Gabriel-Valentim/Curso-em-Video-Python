nota1 = float(input("Quanto é sua primeira nota: "))
nota2 = float(input("Quanto é sua segunda nota: "))

media = (nota1+nota2)/2

if media < 5:
  print("Lamento mas você esta reprovado")
elif  5 <= media <= 6.9:
  print("Você esta de recuperação")
else:
  print("Parabens você passou")