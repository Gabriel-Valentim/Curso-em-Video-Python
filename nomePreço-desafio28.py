totalGasto = 0
maisMil = 0
maisBarato = ""
maisBaratoP = 0

while True:
  nome = str(input("Qual o nome do produto: "))
  preço = int(input("Qual o preço do produto: "))
  continuar = str(input("Você quer continuar [S/N]: "))

  if totalGasto == 0:
    maisBarato = nome
    maisBaratoP = preço

  totalGasto += preço

  if preço > 100:
    maisMil += 1
  
  if maisBaratoP > preço:
    maisBaratoP = preço
    maisBarato = nome

  if continuar == "N":
    break
  
print(f"O preço total foi de {totalGasto}, teve {maisMil} produtos com preços a cima de 1000 reais, e o produto mais barato foi {maisBarato}")