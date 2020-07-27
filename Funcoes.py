import random
import os
import time
from unicodedata import normalize
import interface
global _palavra_secreta,_Palavra_secreta_pontilhada,dica
Lista_Palavras_Usadas = list()
Lista_Letras_Usadas = list()
acerta = []
posicao = []
aux = []

def welcome():
    while True:
        #Mostra tela do menu inicial e retorna o input colocado como opção do tema escolhido
        opcao = int(interface.telaInicial())
        print(opcao)
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6:
            print('SelecionarTema',)
            return SelecionarTema(opcao)
        else:
            print('Opção invalida, tente novamente!')
            
        


def remover_acentos(txt):

    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')   


def verificacao(tentativa):
    global _Palavra_secreta_pontilhada
    if len(tentativa) > 1:  
        if tentativa == _palavra_secreta: 
            venceu=1
            return venceu
        #Não consegui fazer esses prints de testes na interface sem ter que mudar a função inteira, então não coloquei
        elif tentativa in Lista_Palavras_Usadas:  
            print("Palavra ja utilizada!")
        else:  
            print("Essa não é a palavra")
        return 2
    else:# se for letra
        posicao.clear()
        if tentativa in Lista_Letras_Usadas:
            print('Essa letra já foi escolhida')
        elif tentativa not in _palavra_secreta:
            print('Não possui a letra')
            Lista_Letras_Usadas.append(tentativa)
        else:
            Lista_Letras_Usadas.append(tentativa)
            aux = list(_Palavra_secreta_pontilhada)
            for i, letra in enumerate(_palavra_secreta):
                if letra == tentativa:
                    posicao.append(i)
            for index in posicao:
                aux[index*2] = tentativa
            _Palavra_secreta_pontilhada = "".join(aux)
            if '_' not in _Palavra_secreta_pontilhada:
                return 1
            return 3
        return 2
         

def palavraValida(tentativa):
    
    if tentativa.isalpha(): 
        return verificacao(tentativa)
    else: 
        print ("Dado informado não é válido!")
        return 2

#FUNCAO ESTÁ NA INTERFACE
'''def exibirBoneco(vidas): 
    
    if vidas == 5: 
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /             / \ ")
        print("| |/             (   )")
        print("| |               \_/")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
    
    elif vidas == 4:
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /           (× ‿ ×) ")
        print("| |/")
        print("| | ")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
    
    elif vidas == 3:
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /           (× ‿ ×) ")
        print("| |/               |")
        print("| |               ( ) ")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
    
    elif vidas == 2:
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /           (× ‿ ×) ")
        print("| |/               |")
        print("| |              /( )\ ")
        print("| |             /     \ ")
        print("| |            ′      ′ ")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
    
    elif vidas == 1:
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /           (× ‿ ×) ")
        print("| |/               |")
        print("| |              /( )\ ")
        print("| |             /  |  \  ")
        print("| |            ′   |  ′ ")
        print("| |                ∆     ")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
    
    elif vidas == 0:
        print(" _________________________")
        print("/_________________))______/")
        print("| |  / /          ||")
        print("| | / /           ||")
        print("| |/ /            ||")
        print("| | /           (× ‿ ×) ")
        print("| |/               |")
        print("| |              /( )\ ")
        print("| |             /  |  \  ")
        print("| |            ′   |  ′ ")
        print("| |                ∆     ")
        print("| |              /   \    ")
        print("| |             /     \    ")
        print("| |            ‘       ‘   ")
        print("| |")'''

def SelecionarTema(tema):
    if (tema == 1):

        PROFISSÃO = [ 'AGRICULTOR', 'ARQUITETO', 'ASTRONAUTA', 'BOMBEIRO', 'CANTOR',
                    'CABELEREIRO', 'CONTADOR', 'DELEGADO', 'DESIGNER', 'ESCRITOR',
                    'ENFERMEIRO', 'ELETRICISTA', 'FARMACEUTICO', 'FEIRANTE',
                    'FOTOGRÁFO', 'HUMORISTA', 'GARIMPEIRO', 'GERENTE',
                    'GEOGRÁFO', 'INTÉRPRETE', 'JORNALISTA', 'LAVRADOR', 'MÉDICO',
                    'MOTORISTA', 'NUTRICIONISTA', 'OTORRINOLARINGOLOGISTA', 'PADEIRO',
                    'PEDREIRO', 'PROFESSOR', 'POLICIAL', 'QUÍMICO', 'RECEPCIONOSTA',
                    'REDATOR', 'RADIALISTA', 'SUPERVISOR','TAXISTA', 'UROLOGISTA', 'VIGILANTE', 'VENDEDOR']
        return random.choices(PROFISSÃO), "PROFISSÃO"
    elif (tema == 2):

        FRUTAS = [ 'ABACATE', 'ABACAXI', 'AÇAÍ', 'ACEROLA', 'AMEIXA', 'AMORA', 
                 'BANANA', 'CACAU', 'CAJU' , 'CAQUI', 'CEREJA' ,'COCO','DAMASCO',
                 'FIGO' , 'FRAMBOESA' , 'GOIABA' , 'GRAVIOLA' , 'GROSELHA', 
                 'GUARANÁ' , 'JABUTICABA' , 'JACA', 'JAMBO', 'JENIPAPO', 'KIWI', 
                 'LARANJA', 'LIMÃO' ,'LIMA', 'MACÃ','MAMÃO', 'MANGA','MANGABA', 
                 'MARACUJA','MELANCIA', 'MELÃO', 'MEXERICA', 'MORANGO', 'PERA',
                 'PÊSSEGO', 'PITANGA', 'PINHA' , 'PITOMBA', 'PEQUI', 'ROMÃ', 
                 'SERIGUELA', 'TAMARINDO', 'TÂMARA', 'UVA', 'UMBU']
        return random.choices(FRUTAS), "FRUTAS"
   
    elif (tema == 3):

        ANIMAIS = [ 'ANTA','ABELHA', 'ARARA','ALCE','ASNO','BAIACU','BALEIA',
                  'BORBOLETA','CABRA','CACHORRO', 'CAPIVARA','ELEFANTE',
                  'ESQUILO','FAISÃO','GAIVOTA','GALO','HIENA','HAMSTER',
                  'IGUANA','JACARÉ','JABURU','LAGOSTA','LEÃO', 'MACACO',
                  'MURIÇOCA','ORNITORRINCO','OVELHA','PAPAGAIO','PIRANHA',
                  'RAPOSA','ROUXINOL','SUCURI','SARDINHA','TUBARÃO','TUCANO',
                  'TAMANDUÁ','URSO','URUBU', 'VACA','VESPA','VEADO','ZEBRA']
        return random.choices(ANIMAIS), "ANIMAIS"
    elif (tema == 4):

        INSTRUMENTOS = [ 'ALAÚDE','ARCODEÃO','BAIXO','BANDOLIM','BATERIA',
                        'BAIXO', 'CAIXA','CARRILHÃO','CASTANHOLHAS','CHOCALHO',
                        'CLARINETE', 'CLARIM','CÍTARA','CORNETE','FAGOTE',
                        'FLAUTA', 'FLAUTIM','GAITA', 'GUITARRA', 'HARPA',
                        'OBOÉ', 'ORGÃO', 'PANDEIRO','PIANO','PÍFARO','SANFONA',
                        'SAXOFONE','TECLADO','TRIANGULO','TUBA', 'UKULELE',
                        'VIOLÃO', 'VIOLINO','VIOLA','XILOFONE']
        return random.choices(INSTRUMENTOS), "INSTRUMENTOS"

    elif (tema == 5):

        CORES = [  'AZUL', 'ANIL', 'AMETISTA','AMARELO','BRANCO','CINZA',
                'CASTANHO','CIANO','DOURADO','ESMERALDA' ,'FÚCSIA',
                'FERRUGEM', 'JADE','JAMBO','LARANJA','LILÁS','MARROM',
                'MAFIM','MAGNETA','OURO','PRETO','PRATA', 'QUANTUM',
                'ROSA', 'ROXO','SÉPIA', 'SALMÃO','TURQUESA','VERDE','VERMELHO','VIOLETA']
        return random.choices(CORES), "CORES"

    elif (tema == 6):

        RAND = random.randint(1, 5)
        print(RAND)
        v1,v2 = SelecionarTema(RAND)
        return v1,v2
        
def Start(): 
    global _Palavra_secreta_pontilhada,_palavra_secreta, dica
    palavra,dica = welcome()
    numeroRandom = random.randrange(0, len(palavra))
    palavra_Selecionada = palavra[numeroRandom].upper()
    palavra_Selecionada = remover_acentos(palavra_Selecionada)
    return palavra_Selecionada,dica

_palavra_secreta,dica = Start() # armazena a palavra secreta
_Palavra_secreta_pontilhada = "_ " * len(_palavra_secreta) # armazena a palavra secreta só que em vez de letras, em _
#!OK

def reset():
    global _Palavra_secreta_pontilhada,_palavra_secreta
    aux,acerta,Lista_Letras_Usadas.clear(), Lista_Palavras_Usadas.clear(),posicao.clear()
    _Palavra_secreta_pontilhada = " "
    _palavra_secreta = " "
    _palavra_secreta,dica = Start() # armazena a palavra secreta
    _Palavra_secreta_pontilhada = "_ " * len(_palavra_secreta) 