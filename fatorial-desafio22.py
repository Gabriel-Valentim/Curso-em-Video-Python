num = int(input("Digite um numero para descobrir seu fatorial: "))

cont = num - 1
fatorial = num*cont
cont -= 1

while cont != 0:
  fatorial = fatorial * cont
  cont -= 1

print("O fatorial de {} é {}".format(num, fatorial))