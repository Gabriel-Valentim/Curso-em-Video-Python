times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético-PR', 'Bragantino', 'Ceará-SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco', 'Goiáis', 'Coritiba', 'Botafogo')

print(f"Lista de times do brasileirão {times}")

print("Os 5 primeiros colocados são:")

for top5 in range(0, 5):
  print(f"{times[top5]}")

print("Os 4 ultimos colocados são:")

for rebaixados in range(len(times) - 4, len(times)):
  print(f"{times[rebaixados]}")

print(f"Times em ordem alfabetica {sorted(times)}")

procura = str(input("Qual time você quer ver sua posição: "))
print(times.index(procura))