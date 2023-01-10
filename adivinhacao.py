def jogar():
    import random

    print(32*'*')
    print('Bem vindo ao jogo de advinhação!')
    print(32*'*')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    rodada = 1
    pontos_totais = 100

    nivel = int(input('Qual nível de dificuldade deseja? (1)Fácil (2)Médio (3)Difícil: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 5
    elif(nivel == 3):
        total_de_tentativas = 2
    else:
        total_de_tentativas = 1



    for rodada in range (1, total_de_tentativas + 1):
        
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        print('Total de pontos: ', pontos_totais)


        chute_str = input('Digite um número entre 1 e 100: ')
        chute = int(chute_str)
        
        print('Você digitou', chute)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        if(numero_secreto == chute):
            print("Parabéns, você acertou.")
            print('Seu total de pontos foi de: {} '.format(pontos_totais))
            break
        else:
            if(numero_secreto > chute):
                print('Você chutou um número menor')
            else:
                print('Você chutou um número maior')
        print("Tente novamente.")

        pontos_perdidos = abs(chute - numero_secreto) #abs -> transforma o número em absoluto, ou seja, ignora o sinal negativo (similar a um módulo)
        pontos_totais = pontos_totais - pontos_perdidos

        if(pontos_totais <= 0):
            print('Você perdeu todos os pontos. Tente novamente.')
            break

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()