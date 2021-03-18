print("Tabuada")

n = int(input("Qual numero você quer ver a tabuada: "))

for tab in range(1, 11):
  aux = n*tab
  print("{} X {}: {}".format(tab, n, aux))