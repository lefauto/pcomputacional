import zipfile

NOME_ARQUIVO = "senha_bitcoin.zip"
zip_file = zipfile.ZipFile(NOME_ARQUIVO, 'r')


def extrair_arquivo_zip_com_senha(senha):
    try:
        zip_file.extractall(path='.', pwd=senha.encode('utf-8'))
        return True
    except:
        pass
    return False


################################################
# Não alterar linhas acima:
################################################

# Versão com o conteúdo da aula de string

# Definindo variáveis
contador = 0

# Alterando o valor do 1º caractere
for w in range(48, 123):
    if not (91 <= w <= 96 or 58 <= w <= 64):
        char1 = chr(w)

        # Alterando o valor do 2º caractere
        for x in range(48, 123):
            if not (91 <= x <= 96 or 58 <= x <= 64):
                char2 = chr(x)

                # Alterando o valor do 3º caractere
                for y in range(48, 123):
                    if not (91 <= y <= 96 or 58 <= y <= 64):
                        char3 = chr(y)

                        # Processo de filtração de caracteres repetidos
                        if char1 != char2 or char1 != char3:
                            senha = char1 + char2 + char3

                            # Processo de filtraçâo de sequência de números
                            if not ((48 <= w <= 55 and x == (w + 1) and y == (w + 2)) or
                                    (50 <= w <= 57 and x == (w - 1) and y == (w - 2))):

                                # Escrevendo as possíveis senhas
                                senha = char1 + char2 + char3
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
                        for z in range(48, 123):
                            if not (91 <= z <= 96 or 58 <= z <= 64):
                                char4 = chr(z)

                                # Processo de filtração de caracteres repetidos
                                if ((char1 != char2 and (char1 != char3 or char1 != char4) or
                                     (char1 != char3 and (char1 != char2 or char1 != char4)) or
                                     (char1 != char4 and (char1 != char3 or char1 != char2))) and
                                    (char2 != char3 or char2 != char4)):

                                    if not ((48 <= w <= 55 and x == (w + 1) and y == (w + 2) and z == (w + 3)) or
                                            (50 <= w <= 57 and x == (w - 1) and y == (w - 2) and z == w - 3)):

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
