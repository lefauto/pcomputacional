def contador_de_tempo(segundos: int) -> str:
    minutos = segundos // 60
    horas = minutos // 60
    segundos = segundos % 60
    minutos = minutos % 60
    if horas == 0:
        if minutos == 0:
            return f'{segundos}s'
        elif minutos == 1 and segundos == 0:
            return f'{minutos}m'
        else:
            return f'{minutos}m {segundos}s'
    elif horas == 1 and minutos == 0 and segundos == 0:
        return f'{horas}h'
    return f'{horas}h {minutos}m {segundos}s'


print(contador_de_tempo(17))
print(contador_de_tempo(60))
print(contador_de_tempo(2289))
print(contador_de_tempo(3600))
print(contador_de_tempo(94812357))
