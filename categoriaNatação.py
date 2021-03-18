print("Teste para descobrir sua categoria na classe de natação")
anoNascimento = int(input("Qual seu ano de nascimento: "))

categoria = 2021 - anoNascimento

if categoria <= 9:
  print("Cartegoria mirim")
elif categoria <= 14:
  print("Categoria infantil")
elif categoria <= 19:
  print("Categoria junior")
elif categoria <= 20:
  print("Categoria senior")
else:
  print("Categoria master")