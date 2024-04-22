x = 'sim'
while x != "nao":
  ano = int(input("Insira o ano (apenas d.c):"))
  if ano % 4 == 0:
    print("É bissexto.")
    x = input("Deseja continuar? sim/nao")
  else:
    ano = ano + (4 - ano % 4)
    print("Não é bissexto, próximo ano bissexto é", ano)
    x = input("Deseja continuar? sim/nao")
print("Programa encerrado.")
