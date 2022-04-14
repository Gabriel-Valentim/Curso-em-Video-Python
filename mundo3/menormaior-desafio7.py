num = []

for c in range(0, 5):
  num.append(int(input(f"Digite um numero na posição {c}: ")))
  if c == 0:
    maior = num[c]
    menor = num[c]
  else:
    if num[c] < menor:
      menor = num[c]
  
    if num[c] > maior:
      maior = num[c]

print("=-"*30)
print(f"Você digitou os valores {num}") 
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(num):
  if v == maior:
    print(f"{i}...", end='') 

print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(num):
  if v == menor:
    print(f"{i}...", end='')