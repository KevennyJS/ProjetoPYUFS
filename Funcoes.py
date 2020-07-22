import random
import os
import time
from unicodedata import normalize

global _palavra_secreta,_Palavra_secreta_pontilhada,dica

Lista_Palavras_Usadas = list()
Lista_Letras_Usadas = list()
acerta = []
posicao = []
aux = []


def welcome():
    while True:
        print('''
            BEM VINDO AO JOGO DA FORCA
        
        SELECIONE O TEMA:

        [1] PROFISSÃO
        [2] COMIDA
        [3] CORPO HUMANO
        [4] ANIMAIS
        [5] INSTRUMENTOS
        [6]CORES
        [7]ALEATÓRIO

        OPÇÃO: ''',end = '')
        opcao = int(input())
        if opcao > 0 and opcao < 8:
            return SelecionarTema(opcao)
        else:
            print('Opção invalida, tente novamente!')
            time.sleep(2)
            cls()


def remover_acentos(txt):

    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')   

def cls(): 
    os.system("cls")

def verificacao(tentativa):
    global _Palavra_secreta_pontilhada
    
    if len(tentativa) > 1:  
        if tentativa == _palavra_secreta: 
            venceu=1
            return venceu
        elif tentativa in Lista_Palavras_Usadas:  
            print("Palavra ja utilizada!")
        else:  
            print("Essa não é a palavra")
            Lista_Palavras_Usadas.append(tentativa)
        time.sleep(2)
        return 2
    else:# se for letra
        posicao.clear()
        if tentativa in Lista_Letras_Usadas:
            print('Essa letra já foi escolhida')
        elif tentativa not in _palavra_secreta:
            vidas -= 1
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
        time.sleep(2)
        return 2


def palavraValida(tentativa):
    
    if tentativa.isalpha(): 
        return verificacao(tentativa)
    else: 
        print ("Dado informado não é válido!")
        return 2

def exibirBoneco(vidas): 
    
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
        print("| |")

def SelecionarTema(tema):
    if (tema == 1):

        PROFISSÃO = [ 'AGRICULTOR', 'ARQUITETA', 'ASTRONAUTA', 'BOMBEIRO', 'CANTOR', 'CAFEICULTOR',
                    'CABELEREIRO', 'CUTELEIRO', 'CONTADOR', 'DELEGADO', 'DESIGNER', 'ESCRITOR',
                    'ENFERMEIRA', 'ELETRICISTA', 'FARMACEUTICO', 'FEIRANTE', 'FORJADOR',
                    'FOTOGRÁFO', 'HUMORISTA', 'HOMEOPATA', 'GARIMPEIRO', 'GENETICISTA','GERENTE',
                    'GEOGRÁFO', 'ILUSTRADOR','INTÉRPRETE', 'JORNALISTA', 'LUTHIER', 'LAVRADOR', 'MÉDICO',
                    'MOTORISTA', 'NUTRICIONISTA',  'OURIVES', 'OTORRINOLARINGOLOGISTA', 'PADEIRO',
                    'PEDREIRO', 'PROFESSOR', 'POLICIAL', 'QUIROPRAXISTA', 'QUÍMICO', 'RECEPCIONOSTA',
                    'REDATOR', 'RADIALISTA', 'SUSHIMAN', 'SUPERVISOR','TAXISTA', 'UROLOGISTA', 'VIGILANTE', 'VENDEDOR']
        return random.choices(PROFISSÃO), "PROFISSÃO"
    elif (tema == 2):

        COMIDA = [ 'ABACATE','ABACAXI', 'ARROZ', 'BATATA','BISCOITO',
                'BRIGADEIRO', 'CANJICA','CAJU','CHIPS', 'DONUTS',
                'DAMASCO','ERVILHA', 'ESCONDIDINHO','FRANGO','FETTUCCINE',
                'FEIJÃO', 'GRAVIOLA', 'GELEIA','GENGIBRE', 'HAMBURGUER',
                'IOGURTE', 'INHAME','JUJUBA', 'KIWI','LAGOSTA','LINGUIÇA',
                'MACARRONADA','MACAXEIRA','MORANGO','MOQUECA', 'MUSSARELA',
                'OVOMALTINE', 'OMELETE', 'OREGANO', 'OSTRA','PUDIM','PIZZA',
                'QUEIJO', 'QUEIJADINHA', 'QUIABO','ROCAMBOLE', 'SALSICHA',
                'SUSHI','TAIOBA', 'TALHARIM', 'VATAPÁ','VINAGRETE']
        return random.choices(COMIDA)
    elif (tema == 3):

        CORPO = ['ABDOMEN','AMÍGDALA', 'AXILA','ARTICULAÇÃO','ARTÉRIAS', 'BAÇO',
                'BARRIGA', 'BOCA', 'BRAÇO','CABELO','CABEÇA','CANELA','COTVELO',
                'COLUNA','CÓRNEA', 'CORAÇÃO', 'COXA', 'DEDO', 'DENTE', 'DIAFRAGMA',
                'DORSAL', 'ESTOMAGO', 'ENDOCÁRDIO','ESTOMAGO', 'ESQUELETO',
                'EPIDERME', 'FARINGE','FALANGES', 'GARGANTA', 'GENGIVAS', 'GLANDES',
                'HIPODERME', 'ÍRIS', 'INTESTINO', 'JOELHO', 'LÁBIOS', 'LINGUA',
                'LARINGE', 'MAMILOS', 'MÚSCULOS', 'NARIZ','NÁDEGAS']
        return random.choices(CORPO)

    elif (tema == 4):

        ANIMAIS = [ 'ANTA','ABELHA', 'ARARA','ALCE','ASNO','BAIACU','BALEIA',
                    'BORBOLETA','CABRA','CACHORRO', 'CAPIVARA','DROMEDÁRIO',
                    'ELEFANTE','ESQUILO','FAISÃO','GAIVOTA','GALO','HIENA',
                    'HAMSTER','IGUANA','JACARÉ','JABURU','LAGOSTA','LEÃO',
                    'MACACO','MURIÇOCA','ORNITORRINCO','OVELHA','PAPAGAIO',
                    'PIRANHA', 'QUATI','RAPOSA','ROUXINOL','SUCURI','SARDINHA',
                    'TUBARÃO','TUCANO', 'TAMANDUÁ','URSO','URUBU', 'VACA',
                    'VESPA','VEADO','ZEBRA']
        return random.choices(ANIMAIS)
    elif (tema == 5):

        INSTRUMENTOS = [ 'ALAÚDE','ARCODEÃO','BAIXO','BANDOLIM','BATERIA',
                        'BAIXO', 'CAIXA','CARRILHÃO','CASTANHOLHAS','CHOCALHO',
                        'CLARINETE', 'CLARIM','CÍTARA','CORNETE','FAGOTE',
                        'FLAUTA', 'FLAUTIM','GAITA', 'GUITARRA', 'HARPA',
                        'OBOÉ', 'ORGÃO', 'PANDEIRO','PIANO','PÍFARO','SANFONA',
                        'SAXOFONE','TECLADO','TRIANGULO','TUBA', 'UKULELE',
                        'VIOLÃO', 'VIOLINO','VIOLA','XILOFONE']
        return random.choices(ISNTRUMENTOS)

    elif (tema == 6):

        CORES = [  'AZUL', 'ANIL', 'AMETISTA','AMARELO','BRANCO','CINZA',
                'CASTANHO','CIANO','DOURADO','ESMERALDA' ,'FÚCSIA',
                'FERRUGEM', 'JADE','JAMBO','LARANJA','LILÁS','MARROM',
                'MAFIM','MAGNETA','OURO','PRETO','PRATA', 'QUANTUM',
                'ROSA', 'ROXO','SÉPIA', 'SALMÃO','TURQUESA','VERDE','VERMELHO','VIOLETA']
        return random.choices(CORES)

    elif (tema == 7):

        ALEATORIO = ['AGRICULTOR', 'ARQUITETA', 'ASTRONAUTA', 'BOMBEIRO', 'CANTOR', 'CAFEICULTOR','CABELEREIRO', 'CUTELEIRO', 'CONTADOR', 'DELEGADO', 'DESIGNER', 'ESCRITOR',
                    'ENFERMEIRA', 'ELETRICISTA', 'FARMACEUTICO', 'FEIRANTE', 'FORJADOR','FOTOGRÁFO', 'HUMORISTA', 'HOMEOPATA', 'GARIMPEIRO', 'GENETICISTA','GERENTE',
                    'GEOGRÁFO', 'ILUSTRADOR','INTÉRPRETE', 'JORNALISTA', 'LUTHIER', 'LAVRADOR', 'MÉDICO','MOTORISTA', 'NUTRICIONISTA',  'OURIVES', 'OTORRINOLARINGOLOGISTA', 'PADEIRO',
                    'PEDREIRO', 'PROFESSOR', 'POLICIAL', 'QUIROPRAXISTA', 'QUÍMICO', 'RECEPCIONOSTA','REDATOR', 'RADIALISTA', 'SUSHIMAN', 'SUPERVISOR','TAXISTA', 'UROLOGISTA', 'VIGILANTE', 'VENDEDOR',
                    'ABACATE','ABACAXI', 'ARROZ', 'BATATA','BISCOITO','BRIGADEIRO', 'CANJICA','CAJU','CHIPS', 'DONUTS','DAMASCO','ERVILHA', 'ESCONDIDINHO','FRANGO','FETTUCCINE',
                    'FEIJÃO', 'GRAVIOLA', 'GELEIA','GENGIBRE', 'HAMBURGUER','IOGURTE', 'INHAME','JUJUBA', 'KIWI','LAGOSTA','LINGUIÇA',
                    'MACARRONADA','MACAXEIRA','MORANGO','MOQUECA', 'MUSSARELA','OVOMALTINE', 'OMELETE', 'OREGANO', 'OSTRA','PUDIM','PIZZA',
                    'QUEIJO', 'QUEIJADINHA', 'QUIABO','ROCAMBOLE', 'SALSICHA','SUSHI','TAIOBA', 'TALHARIM', 'VATAPÁ','VINAGRETE','ABDOMEN','AMÍGDALA', 'AXILA','ARTICULAÇÃO','ARTÉRIAS', 'BAÇO',
                    'BARRIGA', 'BOCA', 'BRAÇO','CABELO','CABEÇA','CANELA','COTVELO','COLUNA','CÓRNEA', 'CORAÇÃO', 'COXA', 'DEDO', 'DENTE', 'DIAFRAGMA',
                    'DORSAL', 'ESTOMAGO', 'ENDOCÁRDIO','ESTOMAGO', 'ESQUELETO','EPIDERME', 'FARINGE','FALANGES', 'GARGANTA', 'GENGIVAS', 'GLANDES',
                    'HIPODERME', 'ÍRIS', 'INTESTINO', 'JOELHO', 'LÁBIOS', 'LINGUA','LARINGE', 'MAMILOS', 'MÚSCULOS', 'NARIZ','NÁDEGAS','ANTA','ABELHA', 'ARARA','ALCE','ASNO','BAIACU','BALEIA',
                    'BORBOLETA','CABRA','CACHORRO', 'CAPIVARA','DROMEDÁRIO','ELEFANTE','ESQUILO','FAISÃO','GAIVOTA','GALO','HIENA','HAMSTER','IGUANA','JACARÉ','JABURU','LAGOSTA','LEÃO',
                    'MACACO','MURIÇOCA','ORNITORRINCO','OVELHA','PAPAGAIO','PIRANHA', 'QUATI','RAPOSA','ROUXINOL','SUCURI','SARDINHA','TUBARÃO','TUCANO', 'TAMANDUÁ','URSO','URUBU', 'VACA',
                    'VESPA','VEADO','ZEBRA','ALAÚDE','ARCODEÃO','BAIXO','BANDOLIM','BATERIA','BAIXO', 'CAIXA','CARRILHÃO','CASTANHOLHAS','CHOCALHO',
                    'CLARINETE', 'CLARIM','CÍTARA','CORNETE','FAGOTE','FLAUTA', 'FLAUTIM','GAITA', 'GUITARRA', 'HARPA','OBOÉ', 'ORGÃO', 'PANDEIRO','PIANO','PÍFARO','SANFONA',
                    'SAXOFONE','TECLADO','TRIANGULO','TUBA', 'UKULELE','VIOLÃO', 'VIOLINO','VIOLA','XILOFONE','AZUL', 'ANIL', 'AMETISTA','AMARELO','BRANCO','CINZA',
                    'CASTANHO','CIANO','DOURADO','ESMERALDA' ,'FÚCSIA','FERRUGEM', 'JADE','JAMBO','LARANJA','LILÁS','MARROM',
                    'MAFIM','MAGNETA','OURO','PRETO','PRATA', 'QUANTUM','ROSA', 'ROXO','SÉPIA', 'SALMÃO','TURQUESA','VERDE','VERMELHO','VIOLETA']
        return random.choices(ALEATORIO)
        
def Start(): 
    global _Palavra_secreta_pontilhada,_palavra_secreta, dica
    cls()
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
    aux,acerta,Lista_Letras_Usadas,Lista_Palavras_Usadas,posicao.clear()
    _Palavra_secreta_pontilhada = " "
    _palavra_secreta = " "
    _palavra_secreta,dica = Start() # armazena a palavra secreta
    _Palavra_secreta_pontilhada = "_ " * len(_palavra_secreta) 