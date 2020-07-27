import random
import Funcoes
import time
import interface


#--------VARIAVEIS-----------
vidas = 6
fim = 0
#----------------------------


while fim != 1:
    while vidas !=0:
        print(Funcoes._palavra_secreta)
        #Mostra a tela com o boneco, as dica, as vidas e a palavra pontilhada
        tentativa = interface.telaBoneco(Funcoes.dica, str(vidas),Funcoes._Palavra_secreta_pontilhada)
        tentativa = tentativa.upper()
        retorno = Funcoes.palavraValida(tentativa)
        if retorno == 1:
            #mostra a tela ganhou passando a palavra secreta, pergunta se deseja continuar e passa para o reset o que foi digitado no input da tela
            reset = interface.ganhou(Funcoes._palavra_secreta)
            break
        elif retorno == 3:
            continue
        elif retorno == 2:
            vidas -= 1

    if(vidas == 0):
        #mostra a tela perdeu, pergunta se deseja continuar e passa para o reset o que foi digitado no input da tela
        reset = interface.perdeu()
    if reset == '2': 
       fim = 1

    elif reset == '1':
       int(reset)
       Funcoes.reset()
       vidas = 5
       fim = 0
    else:
        fim = 1
    