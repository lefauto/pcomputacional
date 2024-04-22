x = 'sim'
while x != 'nao':
    mes = int(input('Insira o número do seu mês:'))
    if mes >= 1 or mes <= 12:
        match mes:
            case 1:
                    print("Seu signo é Python.")
                    x = input("Deseja continuar? sim/nao")
            case 2:
                    print("Seu signo é Fortran.")
                    x = input("Deseja continuar? sim/nao")
            case 3:
                    print("Seu signo é Rust")
                    x = input("Deseja continuar? sim/nao")
            case 4:
                    print("Seu signo é Go")
                    x = input("Deseja continuar? sim/nao")
            case 5:
                    print("Seu signo é Java")
                    x = input("Deseja continuar? sim/nao")
            case 6:
                    print("Seu signo é JavaScript")
                    x = input("Deseja continuar? sim/nao")
            case 7:
                    print("Seu signo é C")
                    x = input("Deseja continuar? sim/nao")
            case 8:
                    print("Seu signo é PHP")
                    x = input("Deseja continuar? sim/nao")
            case 9:
                    print("Seu signo é Haskell")
                    x = input("Deseja continuar? sim/nao")
            case 10:
                    print("Seu signo é Perl")
                    x = input("Deseja continuar? sim/nao")
            case 11:
                    print("Seu signo é Swift")
                    x = input("Deseja continuar? sim/nao")
            case 12:
                    print("Seu signo é Kotlin")
                    x = input("Deseja continuar? sim/nao")
    else:
        print("Burro.")
        x = input("Deseja continuar?sim/nao")