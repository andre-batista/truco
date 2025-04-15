import enum
from .carta import Carta

class Vencedor(enum.Enum):
    """
    Enumera os possíveis resultados de uma jogada.
    
    Valores:
        A (1): Jogador A venceu.
        B (2): Jogador B venceu.
        Nenhum (0): Empate (nenhum jogador venceu).
    """
    A = 1
    B = 2
    Nenhum = 0

class Jogada:
    """
    Representa uma jogada no jogo de truco, comparando as cartas jogadas.
    
    Esta classe gerencia a comparação entre duas cartas para determinar
    o vencedor de uma rodada individual.
    
    Métodos:
        __init__(): Inicializa uma instância da classe Jogada.
        quem_ganhou(carta_A, carta_B): Determina qual carta vence a jogada.
    """
    
    def __init__(self):
        """
        Inicializa uma nova instância da classe Jogada.
        """
        pass
    
    def quem_ganhou(self, carta_A: Carta, carta_B: Carta) -> Vencedor:
        """
        Determina qual carta vence a jogada com base nos valores das cartas.
        
        Args:
            carta_A (Carta): A carta jogada pelo jogador A.
            carta_B (Carta): A carta jogada pelo jogador B.
            
        Returns:
            Vencedor: Enum indicando qual jogador venceu (A, B ou Nenhum em caso de empate).
        """
        if carta_A > carta_B:
            return Vencedor.A
        elif carta_A < carta_B:
            return Vencedor.B
        else:
            return Vencedor.Nenhum