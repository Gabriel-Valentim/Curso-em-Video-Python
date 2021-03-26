homens = 0
maiorIdade = 0
cont = 0

while True:
  nome = str(input("Digite um nome: "))
  idade = int(input("Digite uma idade: "))
  sexo = str(input("Digite o sexo da pessoa: "))
  continuar = str(input("Você quer continuar [S/N]: "))
  

  if sexo == 'masculino':
    homens += 1
  
  elif sexo == "feminino" and idade < 20:
    cont += 1
  
  if idade > 18:
    maiorIdade += 1
  
  if continuar == "N":
    break



print(f"A quantidade de homens cadastrados é {homens}, tem {maiorIdade} pessoas com mais de 18 anos, e tem {cont} mulheres com menos de 20 anos")