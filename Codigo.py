import random
import Funcoes
import time


#--------VARIAVEIS-----------
vidas = 5
fim = 0
#----------------------------


while fim != 1:
    while vidas !=0:
        Funcoes.cls()
        print("Dica: ",Funcoes.dica)
        Funcoes.exibirBoneco(vidas)
        print(Funcoes._Palavra_secreta_pontilhada,"\n")
        tentativa = input("Tentativa: ").upper()
        retorno = Funcoes.palavraValida(tentativa)
        if retorno == 1:
            Funcoes.cls()
            print(' VOCÊ VENCEU!')
            break
        elif retorno == 3:
            continue
        elif retorno == 2:
            vidas -= 1

    if(vidas == 0):
        Funcoes.cls()
        Funcoes.exibirBoneco(vidas)
        print('\nVOCÊ PERDEU!!')
    print('''
    Deseja jogar novamente?
    [1] SIM
    [2] NÃO
    ''')
    reset = int(input())
    if reset != 1:
        fim = 1
    else:
        Funcoes.reset()
        vidas = 5
        fim = 0