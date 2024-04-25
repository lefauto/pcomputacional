# Processo de filtração para o funcionamento do código
tamanho = 1001
while tamanho >= 1000:
    tamanho = int(input("Insira um número menor de 1000:"))
    if tamanho >= 1000:
        print("Valor inválido.")
    elif tamanho % 2 == 0:
        tamanho += 1
        print("O número inserido era par, usaremos", tamanho, "no seu lugar.")

# Desenha a metade superior do triângulo
espacos = tamanho // 2
for altura in range(tamanho):
    if altura == (tamanho - 1):
        if altura < 10:
            print(("#" * (tamanho // 2)) + str(altura + 1) + ("#" * (tamanho // 2)))
        elif 10 <= altura < 100:
            print(("#" * (tamanho // 2)) + str(altura + 1) + ("#" * ((tamanho // 2) - 1)))
        else:
            print(("#" * ((tamanho // 2) - 1)) + str(altura + 1) + ("#" * ((tamanho // 2) - 1)))
    elif (altura + 1) % 2 == 1:
        print('.' * espacos + "#" * (altura + 1))
        espacos -= 1
 
# Desenha a metade inferior do triângulo
espacos = 0
for altura in range(tamanho - 2):
    if (altura + 1) % 2 == 1:
        espacos += 1
        print('.' * espacos + "#" * ((tamanho - 2) - altura))