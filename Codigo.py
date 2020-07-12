import random
import Funcoes


_palavra_secreta = Funcoes.Start() # armazena a palavra secreta
_Palavra_secreta_pontilhada = "_" * len(_palavra_secreta) # armazena a palavra secreta só que em vez de letras, em _
Funcoes.Lista_Palavras_Usadas.append(_palavra_secreta) #Manda armazenar as palavras que ja foram usadas na lista