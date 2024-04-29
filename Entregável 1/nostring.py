# Versão sem o conteúdo da aula de string
lista1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
char1 = '0'
char2 = '0'
char3 = '1'
char0 = '1'
contador = 0


# Alterando o valor do 1º caractere
for valor1 in range(len(lista1)):
    char1 = lista1[valor1]

    # Alterando o valor do 2º caractere
    for valor2 in range(len(lista1)):
        char2 = lista1[valor2]

        # Alterando o valor do 3º caractere
        for valor3 in range(len(lista1)):
            char3 = lista1[valor3]

            # Processo de filtração de caracteres repetidos
            if char1 != char2 or char1 != char3:
                passtry = char1 + char2 + char3

                # Escrevendo as possíveis senhas
                print(passtry)
                contador += 1

            # Alterando o valor do 4º caractere
            for valor0 in range(len(lista1)):
                char0 = lista1[valor0]

                # Processo de filtração de caracteres repetidos
                if ((char1 != char2 and (char1 != char3 or char1 != char0) or
                   (char1 != char3 and (char1 != char2 or char1 != char0)) or
                   (char1 != char0 and (char1 != char3 or char1 != char2))) and
                   (char2 != char3 or char2 != char0)):

                    # Escrevendo as possíveis senhas
                    passtry = char1 + char2 + char3 + char0
                    print(passtry)
                    contador += 1

print("Número de tentativas:", contador)
