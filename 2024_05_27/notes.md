# Python: Introdução à Funções

## Funções

### Definição
- Um bloco de código reutilizável e autocontido que executa uma tarefa específica. 
````
def nome_da_função(parametro1, parametro2, ...):
    # Corpo da função
    return resultado
````

### Parâmetros e Argumentos
- Parâmetros são valores que a função recebe na sua definição (no caso acima, parametro1 e parametro2)
Quando executamos a função, chamamos esses valores de argumentos.

### Parâmetros posicionais
- De acordo com a posição das variáveis na dentro da função.
````
def helloworld(name, age)
    print(f"Hello World! My name's {name} and I'm {age} years")

helloworld("Pedro", 18)
>>> Hello World! I'm Pedro and I'm 18 years old
````

### Parâmetros nomeados
- Ordem arbitrária dos argumentos.
````
def helloworld(name, age)
    print(f"Hello World! My name's {name} and I'm {age} years")

helloworld(age=18, name="Pedro")
>>> Hello World! I'm Pedro and I'm 18 years old
````

### Parâmetros com valor padrão
- Predefinições
````
def helloworld(name, age = 18)
    print(f"Hello World! My name's {name} and I'm {age} years")

helloworld("Pedro")
>>> Hello World! I'm Pedro and I'm 18 years old

helloworld(Pedro, 28)
>>> Hello World! I'm Pedro and I'm 28 years old
````

### Escopo local de variáveis
- Só pode ser acessado dentro da função
````
def minha_funcao():
    variavel_local = 10
    print(variavel_local)

minha_funcao() # Saída: 10
print(variavel_local) # Erro
````

### Escopo global de variáveis
- Pode ser acessado de qualquer lugar, incluindo dentro de funções
- **Evite** este recurso
````
variavel_global = 10

def minha_funcao():
    global variavel_global
    variavel_global = 20
    print(variavel_global)

minha_funcao() # Saída: 20
print(variavel_global) # Saída: 20
````

### Tipagem de parâmetros
- Boa prática de documentação
````
def minha_funcao(nome: 'entrada') -> 'saída':
    return f"Olá, {nome}!"
````
````
def minha_funcao(nome: str) -> str:
    return f"Olá, {nome}!"

minha_funcao("Pedro") # Saída: Olá, Pedro!
````
````
def minha_funcao(nome: int) -> str:
    return f"Olá, {nome}!"

minha_funcao(30) # Saída: Olá, 30!
````

### Lambda
