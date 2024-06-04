def separa_strings(string: str) -> list:
    listastr1 = []
    for i in range(len(string)):
        listastr1.append(string[i])
    return listastr1


def v_anagrama(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    string1 = separa_strings(string1)
    string2 = separa_strings(string2)
    return sorted(string1) == sorted(string2)


lista = ['b', 'a', 'a', 'd', 'c']
print(sorted(lista))
print(v_anagrama('banana', 'anana'))
print(v_anagrama('carro', 'caroo'))
print(v_anagrama('undertale', 'deltarune'))
