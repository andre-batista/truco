from .ponto import Ponto, TipoPontos
from .jogada import Jogada, Vencedor

class Mao:
    """
    Representa uma mão (rodada) de jogo no truco.
    
    Esta classe gerencia as cartas de cada jogador, o vencedor de cada jogada,
    a pontuação da mão atual e determina quando a mão terminou.
    
    Atributos:
        cartas_A (list): Lista de cartas do jogador A.
        cartas_B (list): Lista de cartas do jogador B.
        vencedor_jogadas (list): Lista de vencedores de cada jogada da mão.
        pontos (Ponto): Pontuação da mão atual.
        vencedor (Vencedor): Armazena quem venceu a mão completa.
    """
    
    def __init__(self):
        """
        Inicializa uma nova instância da classe Mao.
        """
        self.cartas_A = []
        self.cartas_B = []
        self.vencedor_jogadas = []
        self.pontos = Ponto()
        self.vencedor = None

    def coleta_cartas(self, baralho):
        """
        Distribui cartas do baralho para os jogadores A e B.
        
        Args:
            baralho: Objeto baralho que possui método para distribuição de cartas.
        """
        self.cartas_A, self.cartas_B = baralho.distribui_cartas()

    def quem_ganhou_jogada(self, escolha_A: int, escolha_B: int) -> Vencedor:
        """
        Determina o vencedor de uma jogada individual.
        
        Retira as cartas escolhidas das mãos dos jogadores, compara-as
        e registra o resultado.
        
        Args:
            escolha_A (int): Índice da carta escolhida pelo jogador A.
            escolha_B (int): Índice da carta escolhida pelo jogador B.
            
        Returns:
            Vencedor: Enum indicando qual jogador venceu a jogada.
        """
        A = self.cartas_A.pop(escolha_A)
        B = self.cartas_B.pop(escolha_B)
        jogada = Jogada()
        vencedor = jogada.quem_ganhou(A, B)
        self.vencedor_jogadas.append(vencedor)
        return vencedor

    def mao_acabou(self) -> bool:
        """
        Verifica se a mão (rodada) atual terminou.
        
        Uma mão termina quando:
        - Um jogador vence duas jogadas
        - Ocorre um empate após duas jogadas
        - Três jogadas foram realizadas
        
        Returns:
            bool: True se a mão terminou, False caso contrário.
        """
        if len(self.vencedor_jogadas) <= 1:
            return False
        elif len(self.vencedor_jogadas) == 2:
            vitorias_A, vitorias_B = self.conta_vitorias()
            if vitorias_A == 2 or vitorias_B == 2:
                return True
            elif (self.vencedor_jogadas[0] == Vencedor.Nenhum 
                  or self.vencedor_jogadas[1] == Vencedor.Nenhum):
                return True
            else:
                return False
        else:
            return True

    def conta_vitorias(self) -> tuple[int, int]:
        """
        Conta o número de vitórias de cada jogador na mão atual.
        
        Returns:
            tuple[int, int]: Uma tupla com o número de vitórias do jogador A e do jogador B.
        """
        contador_A = self.vencedor_jogadas.count(Vencedor.A)
        contador_B = self.vencedor_jogadas.count(Vencedor.B)
        return contador_A, contador_B

    def quem_ganhou_a_mao(self) -> Vencedor:
        """
        Determina o vencedor da mão atual com base no número de vitórias.
        
        Returns:
            Vencedor: Enum indicando qual jogador venceu a mão, ou Nenhum em caso de empate.
        """
        contador_A = self.vencedor_jogadas.count(Vencedor.A)
        contador_B = self.vencedor_jogadas.count(Vencedor.B)
        if contador_A > contador_B:
            return Vencedor.A
        elif contador_B > contador_A:
            return Vencedor.B
        else:
            return Vencedor.Nenhum

    def quanto_vale_a_mao(self) -> Ponto:
        """
        Retorna o valor atual da pontuação da mão.
        
        Returns:
            Ponto: Objeto Ponto representando o valor atual da mão.
        """
        return self.pontos

    def mao_vale_queda(self) -> bool:
        """
        Verifica se a mão atual vale uma queda (pontuação máxima).
        
        Returns:
            bool: True se a mão vale queda, False caso contrário.
        """
        return self.pontos == Ponto(TipoPontos.Queda)

    def aumenta_pontos(self, valor: Ponto = None) -> None:
        """
        Aumenta o valor da pontuação da mão atual.
        
        Args:
            valor (Ponto, opcional): Valor específico para atualização. 
                Se não for fornecido, aumenta para o próximo nível.
        """
        self.pontos = valor if valor else self.pontos.proximo()