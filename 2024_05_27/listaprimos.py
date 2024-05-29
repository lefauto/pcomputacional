def eh_primo(valor: int) -> bool:
    if valor < 1:
        return False
    for i in range(2, valor):
        if valor % i != 0:
            continue
        else:
            return False
    return True


def lista_primos(valor: int) -> list:
    aux = []
    for i in range(2, valor):
        if eh_primo(i):
            aux.append(i)
    return aux


lista = lista_primos(int(input("Insira um número:")))
print(lista)
