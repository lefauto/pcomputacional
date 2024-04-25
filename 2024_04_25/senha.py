import random

senha = random.randint(0, 10)
tentativa = 0
palpite = 0

while palpite != senha:
    palpite = int(input("Insira a senha:"))
    if palpite != senha:
        print("Senha incorreta.")
    tentativa += 1

print("Acesso garantido")
print("Número de tentativas:", tentativa)
