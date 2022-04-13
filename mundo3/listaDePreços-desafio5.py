produtos = ('Caderno', 10.50,
            'Lapis', 1.50,
            'Caneta', 2.00,
            'Livro', 20.00,
            'Mochila', 34.99,
            'Estojo', 5.00)

print("--------------------------------------------------------")

print("LISTAGEM DE PREÇOS")

print("--------------------------------------------------------")

for c in range(0, len(produtos)):
  if c % 2 == 0 or c == 0:
    print(f"{produtos[c]}........................R$ {produtos[(c+1) % 6]}")

print("--------------------------------------------------------")