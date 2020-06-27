# ProjetoPY(UFS)

## Tópicos

1- Importar Palavras para o programa e armazenar elas em uma lista

2- aplicar uma função RAND na lista para selecionar uma palavra

3- desconcatenar a palavra para que as letras estejam separadas para facilitar a verificação(Lembrando que a palavra atual deve ser mantida em alguma varivel para a verificação em casos do usuario tentar a opção 2 do tópico 5 representado abaixo.

4- perguntar pro usuario quantos jogadores irão participar e adicionar esse valor em uma variavel _QuantJogadores
(OBS: é necessários criar uma variavel para auxiliar a detecção do jogador atual)

5- Iniciar o laço guardando sempre o valor que corresponde ao jogador atual

6- o jogador atual terá 2 opções:
	
	6.1- Tentar uma letra
		se houver a letra na palavra, adiciona a letra e pergunta se ele quer tentar acertar a palavra
			se sim, verificar se são as palavas são iguais.
				se sim, o usuário vence
				senão o usuário perde todas as vidas e é eliminado
			senão, passar a vez para o outro jogador
		se não houver a letra na palavra, o usuário perde uma vida
	6.2- Tentar acerta a palavra(aqui é necessário criar uma função para verificar se aspalavras são correspondentes)

(OBS:)cada jogador possui uma quantidade de vidas X(necessário definir)

(OBS MASTER)com o objetivo de evitar brechas no jogo que possam ser tentadas pelo querido professor para diminuir nossa nota, aplicar a condição de caso a palavra seja formada e nenhum jogador tiver acertado ainda, todos os usuários perdem, o jogo é zerado e uma nova palavra é buscada na lista
