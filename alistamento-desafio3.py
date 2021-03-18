alistou = str(input("Você ja se alistou: "))

if alistou == 'sim':
  print("Parabens você esta em dia com a justiça brasileira")
elif alistou == 'não':
  anoNascimento = int(input("Em que ano você nasceu: "))
  idadeParaAlistar = 2021 - anoNascimento
  
  if idadeParaAlistar == 18:
    print("Você tem que se alistar esse ano")
  elif idadeParaAlistar < 18:
    idadeParaAlistar = 18-idadeParaAlistar
    print("Você ainda não tem idade para se alistar, faltam {} anos".format(idadeParaAlistar))
  elif idadeParaAlistar > 18:
    idadeParaAlistar = idadeParaAlistar-18
    print("Já passou da hora de você se alistar, você esta {} anos atrasado".format(idadeParaAlistar))

else:
  print("Dado invalido")