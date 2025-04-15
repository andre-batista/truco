from truco import Baralho, Jogo, Jogador, Interface
from truco.jogador import TipoJogador

# Criação do baralho
baralho = Baralho("./truco/cartas.csv")

# Criação dos jogadores
jogador1 = Jogador("Jogador 1", tipo=TipoJogador.HUMANO)
jogador2 = Jogador("Jogador 2", tipo=TipoJogador.MAQUINA)

# Criação da interface
interface = Interface()

# Criação do jogo
jogo = Jogo(interface)

# Começo do jogo
jogo.comecar(jogador1, jogador2, baralho)