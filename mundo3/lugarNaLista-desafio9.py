num = []

for c in range(0, 5):
  aux = int(input("Digite um numero: "))
  if c == 0 or aux > num[-1]:
    print("Adicionado no final da lista")
    num.insert(c, aux)
  else:
    pos = 0 
    while pos < len(num):
      if aux <= num[pos]:
        num.insert(pos, aux)
        print(f"Adicionado na posição {pos}")
        break
      pos += 1
    

print(num)