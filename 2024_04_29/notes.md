# Python: String e Random

## Operações
### Interpolation
- Interpolação de strings, também chamado de ‘f-strings’.
- Recurso disponível a partir do Python 3.6 
- Sintaxe: 
    ````
    name = "Alice""
    age = 4
    print(f"Olá, meu nome é {name} e eu tenho {age} anos.") 
    
    # Saída: Olá, meu nome é Alice e eu tenho 4 anos
    ````


### Split
- Divide a string em uma lista de strings, usando o parâmetro como divisor
- Usa ‘ ‘ caso não houver parâmetro
- Sintaxe: 
    ````
    data = "12-03-2024"
    lista_de_numeros = data.splt ("-")  # Saída: ['12', '03', '2024']
    ````


### Slice
- Fatia a string conforme os índices informados 
- Sintaxe:
  ````
    string = 'Python'
    print(string[0])    # Saída: P
    print(string[1:3])  # Saída: yt
    print(string[3:])   # Saída: hon
    print(string[-1])   # Saída: n
  ````
- Operação de slice recebe até 3 parâmetros:
	minha_string[start:stop:step] \
    start: índice do início da fatia \
    stop: índice do final da fatia \
    step: ‘passo’ na fatia 
    ````
    text = ‘Luz azul’
    print(text[::2])    # Saída: Lzau
    print(text[::-1])   # Saída: luza zuL
    ````


### Join
- Une os elementos de uma lista, usando uma string como separador.
    ````
    lista = ["laranja", "maçã", "banana"]

    frutas = ", ".join(lista)   # Saída: 


### Replace
- Substitui ocorrências de uma string por outra string.
    ````
    frase = "Python é uma linguagem de programação"
    novafrase = frase.replace ("linguagem", "laranja")  # Python é uma laranja de programação
    ````


### Find
- Procura por uma substring dentro da string. Retorna o índice da primeira ocorrência ou -1 se não encontrar
    ````
    texto = "Python é uma linguagem de programação"
    posicao = texto.find("linguagem")   # Saída: 12
    posicao = texto.find("laranja")     # Saída: -1
    ````


### Upper, Lower e Capitalize
- Não transforma uma string autal, mas sim gera uma nova
    ````
    texto = "Python é uma Linguagem de Programação"
    texto_min = texto.lower()
    print(texto_min)    ## Saída: python é uma linguagem de programação

    texto_max = texto.upper()
    print(texto_max)    # Saída: PYTHON É UMA LINGUAGEM DE PROGRAMAÇÃO

    texto_cap = texto.capitalize()
    print(texto_cap)    # Saída: Python é uma linguagem de programação
    ````


#
