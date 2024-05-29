def soma_pares(nums: list, alvo: int) -> bool:
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x] + nums[y] == alvo:
                return True
    return False


lista = []
check = 's'
while check != 'n':
    lista.append(int(input("Insira um número para adicionar à lista:")))
    check = input("Deseja adicionar mais um número? s/n")

result = soma_pares(lista, int(input("Insira um alvo:")))
print(result)
