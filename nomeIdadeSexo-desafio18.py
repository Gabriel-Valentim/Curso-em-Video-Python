somaIdade = 0
maiorIdade = 0
cont = 0

for i in range(0, 4):
  nome = str(input("Digite um nome: "))
  idade = int(input("Digite uma idade: "))
  sexo = str(input("Digite o sexo da pessoa: "))
  
  somaIdade += idade

  if maiorIdade < idade and sexo == 'masculino':
    maiorIdade = idade
  
  if sexo == "feminino" and idade < 20:
    cont += 1


media = somaIdade/4

print("A media das idades é {}, o homem mas velho tem {} anos, e tem {} mulheres com menos de 20 anos".format(media, maiorIdade, cont))