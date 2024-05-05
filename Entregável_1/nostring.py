# Versão sem o conteúdo da aula de string

# Definindo variáveis
listabase = [
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
    ]

contador = 0


# Alterando o valor do 1º caractere
for w in range(len(listabase)):
    for valor1 in range(len(listabase[w])):
        char1 = listabase[w][valor1]

        # Alterando o valor do 2º caractere
        for x in range(len(listabase)):
            for valor2 in range(len(listabase[x])):
                char2 = listabase[x][valor2]

                # Alterando o valor do 3º caractere
                for y in range(len(listabase)):
                    for valor3 in range(len(listabase[y])):
                        char3 = listabase[y][valor3]

                        # Processo de filtração de caracteres repetidos
                        if char1 != char2 or char1 != char3:
                            senha = char1 + char2 + char3

                            # Escrevendo as possíveis senhas
                            contador += 1
                            extraido = extrair_arquivo_zip_com_senha(senha)
                            if extraido:
                                print(senha)
                                print('Arquivo extraido')
                                print("Número de tentativas:", contador)
                                exit()
                            else:
                                print(senha)

                        # Alterando o valor do 4º caractere
                        for z in range(len(listabase)):
                            for valor4 in range(len(listabase[z])):
                                char4 = listabase[z][valor4]

                                # Processo de filtração de caracteres repetidos
                                if ((char1 != char2 and (char1 != char3 or char1 != char4) or
                                     (char1 != char3 and (char1 != char2 or char1 != char4)) or
                                     (char1 != char4 and (char1 != char3 or char1 != char2))) and
                                   (char2 != char3 or char2 != char4)):

                                    # Escrevendo as possíveis senhas
                                    senha = char1 + char2 + char3 + char4
                                    contador += 1
                                    extraido = extrair_arquivo_zip_com_senha(senha)
                                    if extraido:
                                        print(senha)
                                        print('Arquivo extraido')
                                        print("Número de tentativas:", contador)
                                        exit()
                                    else:
                                        print(senha)