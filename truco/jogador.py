from enum import Enum
from .ponto import Ponto
from .jogada import Vencedor

class TipoJogador(Enum):
    """
    Enumera os tipos possíveis de jogador.
    
    Valores:
        HUMANO (1): Representa um jogador humano.
        MAQUINA (2): Representa um jogador controlado pelo computador.
    """
    HUMANO = 1
    MAQUINA = 2

class Jogador:
    """
    Representa um jogador no jogo de truco.
    
    Esta classe armazena informações sobre o jogador, incluindo seu nome,
    tipo (humano ou máquina), pontuação e identificador.
    
    Atributos:
        nome (str): O nome do jogador.
        tipo (TipoJogador): O tipo do jogador (humano ou máquina).
        pontos (int): A pontuação atual do jogador.
        id (Vencedor): O identificador do jogador no jogo.
        
    Métodos:
        __init__(nome, tipo): Inicializa uma instância da classe Jogador.
        iniciar_pontos(): Reinicia a pontuação do jogador para zero.
        adicionar_id(iden): Atribui um identificador ao jogador.
        aumentar_pontos(pontos): Incrementa a pontuação do jogador.
        __str__(): Retorna uma representação em string do jogador (nome).
        __repr__(): Retorna uma representação detalhada do jogador para depuração.
    """
    
    def __init__(self, nome: str, tipo: TipoJogador = TipoJogador.HUMANO):
        """
        Inicializa uma nova instância da classe Jogador.
        
        Args:
            nome (str): O nome do jogador.
            tipo (TipoJogador, opcional): O tipo do jogador. Padrão é TipoJogador.HUMANO.
        """
        self.nome = nome
        self.tipo = tipo
        self.pontos = 0
        self.id = None

    def iniciar_pontos(self):
        """
        Reinicia a pontuação do jogador para zero.
        """
        self.pontos = 0
    
    def adicionar_id(self, iden: Vencedor):
        """
        Atribui um identificador ao jogador.
        
        Args:
            iden (Vencedor): O identificador a ser atribuído ao jogador.
        """
        self.id = iden
    
    def aumentar_pontos(self, pontos: Ponto):
        """
        Incrementa a pontuação do jogador.
        
        Args:
            pontos (Ponto): O objeto Ponto contendo o valor a ser adicionado à pontuação.
        """
        self.pontos += pontos.retorna_valor()

    def __str__(self):
        """
        Retorna uma representação em string do jogador.
        
        Returns:
            str: O nome do jogador.
        """
        return f"{self.nome}"

    def __repr__(self):
        """
        Retorna uma representação detalhada do jogador para depuração.
        
        Returns:
            str: Uma string no formato "Jogador(nome, pontos)".
        """
        return f"Jogador({self.nome}, {self.pontos})"