def escolhe_jogo():
    import adivinhacao
    import forca

    print(16*'*')
    print('Escolha um jogo!')
    print(16*'*')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Jogo: '))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()