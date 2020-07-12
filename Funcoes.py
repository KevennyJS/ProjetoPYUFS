import random
import os

Lista_Palavras_Usadas = [ ] #Armazena as palavras que já foram usadas

def Start(): #seleciona uma palavra da lista
    palavra = random.choices(Lista_Palavras)
    numeroRandom = random.randrange(0, len(palavra))
    palavra_Selecionada = palavra[numeroRandom].upper()
    return palavra_Selecionada

def cls(): #Limpa tela
    os.system("cls")

def exibirBoneco(vidas): #
    #estagio = [ 
    #Forca Inicial
    if vidas == 0: 
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

    #Forca 1
    elif vidas == 1:
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

    #Forca 2
    elif vidas == 2:
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

    #Forca 3
    elif vidas == 3:
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

    #Forca 4
    elif vidas == 4:
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

    #Forca 5
    elif vidas == 5:
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
    #]

Lista_Palavras = [
    #PROFISSÃO
    'AGRICULTOR',
    'ARQUITETA',
    'ASTRONAUTA',
    'BOMBEIRO',
    'CANTOR',
    'CAFEICULTOR',
    'CABELEREIRO',
    'CUTELEIRO',
    'CONTADOR',
    'DELEGADO',
    'DESIGNER',
    'ESCRITOR',
    'ENFERMEIRA',
    'ELETRICISTA',
    'FARMACEUTICO',
    'FEIRANTE',
    'FORJADOR',
    'FOTOGRÁFO',
    'HUMORISTA',
    'HOMEOPATA',
    'GARIMPEIRO',
    'GENETICISTA',
    'GERENTE',
    'GEOGRÁFO',
    'ILUSTRADOR',
    'INTÉRPRETE',
    'JORNALISTA',
    'LUTHIER',
    'LAVRADOR',
    'MÉDICO',
    'MOTORISTA',
    'NUTRICIONISTA',
    'OURIVES',
    'OTORRINOLARINGOLOGISTA',
    'PADEIRO',
    'PEDREIRO',
    'PROFESSOR',
    'POLICIAL',
    'QUIROPRAXISTA',
    'QUÍMICO',
    'RECEPCIONOSTA',
    'REDATOR',
    'RADIALISTA',
    'SUSHIMAN',
    'SUPERVISOR',
    'TAXISTA',
    'UROLOGISTA',
    'VIGILANTE',
    'VENDEDOR',
     #COMIDA
    'ABACATE',
    'ABACAXI',
    'ARROZ',
    'BATATA',
    'BISCOITO',
    'BRIGADEIRO',
    'CANJICA',
    'CAJU',
    'CHIPS',
    'DONUTS',
    'DAMASCO',
    'ERVILHA',
    'ESCONDIDINHO',
    'FRANGO',
    'FETTUCCINE',
    'FEIJÃO',
    'GRAVIOLA',
    'GELEIA',
    'GENGIBRE',
    'HAMBURGUER',
    'IOGURTE',
    'INHAME',
    'JUJUBA',
    'KIWI',
    'LAGOSTA',
    'LINGUIÇA',
    'MACARRONADA',
    'MACAXEIRA',
    'MORANGO',
    'MOQUECA',
    'MUSSARELA',
    'OVOMALTINE',
    'OMELETE',
    'OREGANO',
    'OSTRA',
    'PUDIM',
    'PIZZA',
    'QUEIJO',
    'QUEIJADINHA',
    'QUIABO',
    'ROCAMBOLE',
    'SALSICHA',
    'SUSHI',
    'TAIOBA',
    'TALHARIM',
    'VATAPÁ',
    'VINAGRETE',
    #CORPO HUMANO
    'ABDOMEN',
    'AMÍGDALA',
    'AXILA',
    'ARTICULAÇÃO',
    'ARTÉRIAS',
    'BAÇO',
    'BARRIGA',
    'BOCA',
    'BRAÇO',
    'CABELO',
    'CABEÇA',
    'CANELA',
    'COTVELO',
    'COLUNA',
    'CÓRNEA',
    'CORAÇÃO',
    'COXA',
    'DEDO',
    'DENTE',
    'DIAFRAGMA',
    'DORSAL',
    'ESTOMAGO',
    'ENDOCÁRDIO',
    'ESTOMAGO',
    'ESQUELETO',
    'EPIDERME',
    'FARINGE',
    'FALANGES',
    'GARGANTA',
    'GENGIVAS',
    'GLANDES',
    'HIPODERME',
    'ÍRIS',
    'INTESTINO',
    'JOELHO',
    'LÁBIOS',
    'LINGUA',
    'LARINGE',
    'MAMILOS',
    'MÚSCULOS',
    'NARIZ',
    'NÁDEGAS',
    #ANIMAIS
    'ANTA',
    'ABELHA',
    'ARARA',
    'ALCE',
    'ASNO',
    'BAIACU',
    'BALEIA',
    'BORBOLETA',
    'CABRA',
    'CACHORRO',
    'CAPIVARA',
    'DROMEDÁRIO',
    'ELEFANTE',
    'ESQUILO',
    'FAISÃO',
    'GAIVOTA',
    'GALO',
    'HIENA',
    'HAMSTER',
    'IGUANA',
    'JACARÉ',
    'JABURU',
    'LAGOSTA',
    'LEÃO',
    'MACACO',
    'MURIÇOCA',
    'ORNITORRINCO',
    'OVELHA',
    'PAPAGAIO',
    'PIRANHA',
    'QUATI',
    'RAPOSA',
    'ROUXINOL',
    'SUCURI',
    'SARDINHA',
    'TUBARÃO',
    'TUCANO',
    'TAMANDUÁ',
    'URSO',
    'URUBU',
    'VACA',
    'VESPA',
    'VEADO',
    'ZEBRA',
    #INSTRUMENTOS MUSICAIS
    'ALAÚDE',
    'ARCODEÃO',
    'BAIXO',
    'BANDOLIM',
    'BATERIA',
    'BAIXO',
    'CAIXA',
    'CARRILHÃO',
    'CASTANHOLHAS',
    'CHOCALHO',
    'CLARINETE',
    'CLARIM',
    'CÍTARA',
    'CORNETE',
    'FAGOTE',
    'FLAUTA',
    'FLAUTIM',
    'GAITA',
    'GUITARRA',
    'HARPA',
    'OBOÉ',
    'ORGÃO',
    'PANDEIRO',
    'PIANO',
    'PÍFARO',
    'SANFONA',
    'SINTETIZADOR',
    'SAXOFONE',
    'TECLADO',
    'TRIANGULO',
    'TUBA',
    'UKULELE',
    'VIOLÃO',
    'VIOLINO',
    'VIOLA',
    'XILOFONE',
    #CORES 
    'AZUL',
    'ANIL',
    'AMETISTA',
    'AMARELO',
    'BRANCO',
    'CINZA',
    'CASTANHO',
    'CIANO',
    'DOURADO',
    'ESMERALDA' ,
    'FÚCSIA',
    'FERRUGEM',
    'JADE',
    'JAMBO',
    'LARANJA',
    'LILÁS',
    'MARROM',
    'MAFIM',
    'MAGNETA',
    'OURO',
    'PRETO',
    'PRATA',
    'QUANTUM',
    'ROSA',
    'ROXO',
    'SÉPIA',
    'SALMÃO',
    'TURQUESA',
    'VERDE',
    'VERMELHO',
    'VIOLETA']