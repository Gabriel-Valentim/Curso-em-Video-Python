palavras = ('saber', 'aprender', 'ler', 'assistir', 'ver',
            'querer', 'material', 'manga', 'anime', 'latim',
            'dente', 'deitado')

for p in palavras:
  print(f"\nNa palavra {p.upper()} temos ", end='')
  for letra in p:
    if letra.lower() in "aeiou":
      print(letra, end=' ')