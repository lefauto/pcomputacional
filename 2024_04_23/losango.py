tamanho = int(input("Insira um número (3,5,7,9,...):"))
espacos = tamanho // 2
for altura in range(tamanho):
    if (altura + 1) % 2 == 1:
        print('.' * espacos + "#" * (altura + 1))
        espacos -= 1
espacos = 0
for altura in range(tamanho - 2):
    if (altura + 1) % 2 == 1:
        espacos += 1
        print('.' * espacos + "#" * ((tamanho - 2) - altura))