print("Emprestimo Bancario")
valorCasa = float(input("Qual o valor da casa que você deseja comprar: "))
salario = float(input("Quanto é o seu salario: "))
anosParaPagar = int(input("Em quantos anos deseja parcelar o pagamento: "))

anosParaPagar = anosParaPagar*12

salario = salario*30
salario = salario/100

valorMensal = valorCasa/anosParaPagar
valorMensal = valorMensal*30
valorMensal = valorMensal/100

if valorMensal <= salario:
  print("Parabens seu emprestimo foi aprovado")
else:
  print("Lamento mas seu emprestimo não foi aprovado")