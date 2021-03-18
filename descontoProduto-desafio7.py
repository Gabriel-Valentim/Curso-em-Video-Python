print("Compra do produto")
preço = float(input("Qual o preço do produto: "))
metodoDePagamento = str(input("Qual vai ser o metodo de pagamento: "))

if metodoDePagamento == "á vista" or metodoDePagamento == "no cheque":
  desconto = (preço*10)/100
  preço = preço - desconto
  print("Você teve dez porcento de desconto, agora o novo preço é: {}".format(preço))

elif metodoDePagamento == "no cartão":
  vezes = int(input("Em quantas vezes você quer parcelar: "))
  
  if vezes == 1:
    desconto = (preço*5)/100
    preço = preço - desconto
    print("Você teve cinco porcento de desconto, agora o novo preço é: {}".format(preço))

  elif vezes <= 2:
    print("O preço do produto parcelado em 2 vezes é: {}".format(preço))

  elif 3 <= vezes:
    juros = (preço*20)/100
    preço = preço + juros
    print("Parcelando o produto em {} vezes ele passa a valer: {}".format(vezes, preço))
else:
  print("Metodo de compra invalido")