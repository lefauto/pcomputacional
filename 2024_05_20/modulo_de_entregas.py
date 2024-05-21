# Versão de código sem usar a biblioteca requests

cep = '91110000'

# Trecho abaixo não precisa ser alterado
import http.client
import json

# Definindo a constante do tamanho do CEP
LEN_CEP = 8

# Definindo variáveis
contador_consultas = 0
enderecos = {}

while True:
    cep = input('Digite o seu cep (0 para encerrar):')
    if cep == '0':
        break

    if len(cep) != LEN_CEP:  # Verificando o tamanho do CEP inserido
        print('CEP inválido')
        continue

    is_valid = True
    for char in cep:
        if not char.isdigit():  # Verificando os dígitos do CEP inserido
            is_valid = False

    if not is_valid:
        print('CEP inválido')
        continue

    if contador_consultas != 0:
        if cep in enderecos[uf][localidade]:  # Verificando CEPs repetidos
            print('Já sabemos esta consulta')
            continue

    contador_consultas += 1

    url = f"/ws/{cep}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()

    # Adicionando os endereços ao dicionário
    uf = response['uf']
    localidade = response['localidade']

    if uf in enderecos:
        if localidade in enderecos[uf]:
            enderecos[uf][localidade].append(cep)
        else:
            enderecos[uf][localidade] = [cep]
    else:
        enderecos[uf] = {localidade: [cep]}

print("Você consultou um total de:", contador_consultas, "vezes")
print(enderecos)
