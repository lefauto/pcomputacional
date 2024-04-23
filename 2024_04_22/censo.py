idade = int(input("Qual a sua idade?"))
if idade < 0 or idade > 150:
    print("Reprovado")
    exit()
estuda = input("Você estuda? s/n")
if idade < 14 and estuda == 'n':
    print("Aprovado com ressalvas")
    exit()
trabalho = input("Você trabalha? s/n")
if trabalho == 's':
    if idade < 14:
        print("Reprovado")
    elif 14 <= idade <= 16:
        print("Aprovado com ressalvas")
    else:
        regime = input("Qual o seu regime? mei/estag/outro")
        renda = float(input("Qual a sua renda mensal?"))
        if renda < 0:
            print("Reprovado")
        else:
            match regime:
                case 'mei':
                    if renda <= 6750:
                        print("Aprovado")
                    else:
                        print("Reprovado")
                case 'estag':
                    if estuda == 's':
                        print("Aprovado")
                    else:
                        print("Reprovado")
                case 'outro':
                    print("Aprovado")
else:
    aposentado = input("Está aposentado? s/n")
    match aposentado:
        case 's':
            if idade >= 62:
                print("Aprovado")
            else:
                print("Aprovado com ressalvas")
        case 'n':
            print("Aprovado")
