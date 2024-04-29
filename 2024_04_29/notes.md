# Python: String e Random

## Operações
### Concatenação 


### Interpolation
- Interpolação de strings, também chamado de ‘f-strings’.
- Recurso disponível a partir do Python 3.6 
- Sintaxe: 
    ````
    name = "Alice"
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

    frutas = ", ".join(lista)   # Saída: laranja, maçã, banana
    ````


### Replace
- Substitui ocorrências de uma string por outra string.
    ````
    frase = "Python é uma linguagem de programação"
    novafrase = frase.replace ("linguagem", "laranja")  
    
    # Saída: Python é uma laranja de programação
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


## ASCII
- American Standard Code for Information Interchange representa os caracteres alfabéticos, numéricos, pontuação e símbolos. 

- Desenvolvido nos anos 60 e padronizado em 1963 pela ANSI (American National Standards Institute).

- Consiste em 128 caracteres (de 0 a 127). \
  Exemplos: 
  - Letras maiúsculas: A-Z (65-90)
  - Letras minúsculas: a-z (97-122)
  - Números: 0-9 (48-57)

- Limitações:
  - Falta de suporte para caracteres acentuados
  - caracteres não alfabéticos usados em outros idiomas
  - caracteres especiais.  

- Para superar essas limitações, foram desenvolvidas extensões do ASCII, como o ISO 8859 e o UTF-8

### ord e chr
- rd(): Retorna o código ASCII de um caractere
    ````
    print(ord('a')) # Saída: 97
    print(ord('A')) # Saída: 65
    print(ord('0')) # Saída: 48
    ````

- chr(): retorna o caractere correspondente a um número (código ASCII)
    ````
    print(ord('97')) # Saída: a
    print(ord('65')) # Saída: A
    print(ord('47')) # Saída: 0
    ````

## Geração de dados pseudoaleatórios
````
import random


# Gerar um número aleatório entre 0.0 e 1.0
numero_aleatorio = random.random()  
print(numero_aleatorio)     # Saída: Um número aleatório entre 0.0 e 1.0


# Gerar um número inteiro aleatório entre x e y
numero_inteiro = random.randint(1, 100)
print(numero_inteiro)     # Saída: Um número inteiro aleatório entre 1 e 100


# Gerar um número real aleatório entre x e y
numero_real = random.uniform(0.0, 10.0)
print(numero_real)     # Saída: Um número real aleatório entre 0.0 e 10.0


# Escolher um elemento aleatório de uma lista
lista = [0, 1, 2, 3, 4]
elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)     # Saída: Um elemento aleatório da lista


# Embaralhar uma lista
lista_embaralhada = random.sample(lista, len(lista))
print(lista_embaralhada)     # Saída: A lista original embaralhada
````
