import random
num = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

for c in range(0, 5):
  if c == 0:
    maior = num[c]
    menor = num[c]

  if menor > num[c]:
    menor = num[c] 
  if maior < num[c]:
    maior = num[c]

print(f"Os números sorteados foram {num}")
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")