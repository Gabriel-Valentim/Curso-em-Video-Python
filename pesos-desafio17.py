print("Mostra o maior e o menor peso")

maiorPeso = 0
menorPeso = 0

for i in range(0, 5):
  pesos = float(input("Digite um peso: "))
  if pesos > maiorPeso:
    maiorPeso = pesos
  if pesos < menorPeso or i == 0:
    menorPeso = pesos

print("O maior peso foi de {}, e o menor foi {}".format(maiorPeso, menorPeso))