# Python: Dicionários

## Definição
- Estrutura de dados que armazena uma coleção de pares de chaves (key) para valores (value), esses, de qualquer tipo, como strings, inteiros, listas, tuplas e até mesmo outros dicionários.

## Sintaxe
````
variável_dicionário = {
    "variável_lista": {
        "variável1": valor1,
        "variável2": valor2
   }
    "variável3": valor3
}
````
````
print(variável_dicionário["variável_lista"]["variável1"])
# Saída: valor1
print(variável_dicionário["variável3"])
# Saída: valor3
variável_dicionário["variável_lista"]["variável2"] = valor02
print(variável_dicionário["variável_lista"]["variável2"])
# Saída: valor02
````

### Remoção de atributos
- **del**: apenas remove a chave (sem retornar)
- **pop**: remove a chave e retorna o valor

````
del variável_dicionário[variável_lista][variável2]
# Apenas remove a chave
````
````
del variável_dicionário[variável_lista][variável4]
# KeyError
````
````
variável_dicionário.pop["variável_lista"]["variável2"]
# Remove a chave da lista
# Saída: valor2
````

### Iteração
````
for key in variavél_dicionário:
    print(key)
    # Saída: variável_lista
    # Saída: variável3
````
````
for value in variavél_dicionário["variável_lista"].values():
    print(value)
    # Saída: valor1
    # Saída: valor2
````
````
for key. value in variavél_dicionário["variável_lista"].items():
    print(key, value)
    # Saída: variável1 valor1
    # Saída: variável1 valor2
````

### Atualizando dados
````
notas = {"João": 8.5,  "Maria": 7.4}
notas.update({"João": 9.1}) # {"João": 9.1,  "Maria": 7.4}
notas.update({"José": 8.7}) # {"João": 9.1,  "Maria": 7.4, "José": 8.7}
````

### Notas Gerais
- pode se usar "is" no lugar de "=="
