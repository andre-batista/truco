from .mao import Mao
from .baralho import Baralho
from .jogador import Jogador, TipoJogador
from numpy.random import randint, rand
from .carta import Carta
from .ponto import TipoPontos, Ponto
from enum import Enum

class TipoRespostaTruco(Enum):
    """
    Enumera os tipos possíveis de resposta a um pedido de truco.
    
    Valores:
        ACEITAR (1): Aceitar a proposta de aumento de pontos.
        CORRER (2): Desistir da mão atual.
        AUMENTAR (3): Propor um aumento maior de pontos.
    """
    ACEITAR = 1
    CORRER = 2
    AUMENTAR = 3

class Interface:
    """
    Gerencia a interface de interação com os jogadores durante o jogo de truco.
    
    Esta classe contém métodos para apresentar informações ao jogador, obter suas
    escolhas e mostrar o estado do jogo.
    
    Métodos:
        __init__(): Inicializa a interface.
        escolhe_carta(jogador, cartas): Solicita ao jogador que escolha uma carta.
        resposta_ao_truco(jogador_proponente, jogador_resposta, valor): Obtém resposta ao pedido de truco.
        mostra_vencedor(jogador): Exibe o vencedor do jogo.
        informa_quem_abre(jogador): Informa qual jogador inicia a mão.
        pergunta_truco(jogador_proponente, valor): Pergunta se um jogador quer pedir truco.
        informa_placar_jogo(jogador_A, jogador_B): Exibe o placar geral do jogo.
        informa_placar_mao(jogador_A, jogador_B, mao): Exibe o placar da mão atual.
        informa_quem_correu(jogador): Informa qual jogador correu.
        mostra_mao(jogador, mao): Exibe as cartas na mão de um jogador.
    """
    
    def __init__(self):
        """
        Inicializa uma nova instância da classe Interface.
        """
        pass

    def escolhe_carta(self, jogador: Jogador, cartas: list[Carta]) -> int:
        """
        Solicita ao jogador que escolha uma carta entre as disponíveis.
        
        Para jogadores humanos, apresenta as cartas e solicita uma entrada.
        Para jogadores máquina, escolhe aleatoriamente.
        
        Args:
            jogador (Jogador): O jogador que fará a escolha.
            cartas (list[Carta]): Lista de cartas disponíveis para escolha.
            
        Returns:
            int: Índice da carta escolhida na lista.
        """
        if jogador.tipo == TipoJogador.HUMANO:
            print(f"{jogador.nome}, escolha uma carta:")
            for i, carta in enumerate(cartas):
                print(f"{i}: {carta.nome}")
            escolha = int(input("Digite o número da carta: "))
            while escolha < 0 or escolha >= len(cartas):
                print("Escolha inválida. Tente novamente.")
                escolha = int(input("Digite o número da carta: "))
                
        elif jogador.tipo == TipoJogador.MAQUINA:
            escolha = randint(0, len(cartas))
            print(f"{jogador.nome} escolheu a carta: {cartas[escolha].nome}")
         
        return escolha

    def resposta_ao_truco(self, jogador_proponente, jogador_resposta, valor):
        """
        Processa a resposta a um pedido de truco.
        
        Args:
            jogador_proponente (Jogador): Jogador que propôs o truco.
            jogador_resposta (Jogador): Jogador que responderá ao pedido.
            valor (Ponto): Valor atual dos pontos da mão.
            
        Returns:
            tuple: Uma tupla contendo (resposta, valor_atualizado, id_de_quem_correu).
                resposta: Tipo de resposta dada (ACEITAR, CORRER ou AUMENTAR).
                valor_atualizado: Novo valor dos pontos da mão.
                id_de_quem_correu: ID do jogador que correu, ou None.
        """
        quem_correu = None
        
        if jogador_resposta.tipo == TipoJogador.HUMANO:
            
            print(f"O jogador {jogador_proponente.nome} "
                  f"pediu {valor.proximo()}!"
                  f" {jogador_resposta.nome}, o que você deseja fazer?")
            print(f"1: Aceitar {valor.proximo()}")
            print(f"2: Correr")
            
            if valor.proximo().valor != TipoPontos.Queda:
                print(f"3: Pedir {valor.proximo().proximo()}")
                respostas_possiveis = ['1', '2', '3']
            else:
                respostas_possiveis = ['1', '2']
                
            resposta = input("Escolha uma opção: ").strip()
            while resposta not in respostas_possiveis:
                print("Opção inválida. Tente novamente.")
                resposta = input("Escolha uma opção: ").strip()
                
        elif jogador_resposta.tipo == TipoJogador.MAQUINA:
            escolha = rand()
            if valor.proximo().valor != TipoPontos.Queda:
                if escolha < .33:
                    resposta = '1'
                    print(f"Jogador {jogador_resposta.nome} "
                          f"aceitou {valor.proximo()}!")
                elif escolha < .66:
                    resposta = '2'
                    print(f"Jogador {jogador_resposta.nome} "
                          f"correu!")
                else:
                    resposta = '3'
                    print(f"Jogador {jogador_resposta.nome} "
                          f"pediu {valor.proximo().proximo()}!")
            else:
                if escolha < .5:
                    resposta = '1'
                    print(f"Jogador {jogador_resposta.nome} "
                          f"aceitou {valor.proximo()}!")
                else:
                    resposta = '2'
                    print(f"Jogador {jogador_resposta.nome} correu!")
            
        if resposta == '1':
            resposta = TipoRespostaTruco.ACEITAR
            valor = valor.proximo()
        elif resposta == '2':
            resposta = TipoRespostaTruco.CORRER
            quem_correu = jogador_resposta.id
        elif resposta == '3':
            resposta = TipoRespostaTruco.AUMENTAR
            resposta, valor, quem_correu = self.resposta_ao_truco(
                jogador_resposta, jogador_proponente, valor.proximo()
            )
        
        return resposta, valor, quem_correu

    def mostra_vencedor(self, jogador: Jogador):
        """
        Exibe o jogador vencedor e sua pontuação.
        
        Args:
            jogador (Jogador): O jogador vencedor.
        """
        print(f"Vencedor: {jogador.nome} com {jogador.pontos} pontos!")

    def informa_quem_abre(self, jogador: Jogador):
        """
        Informa qual jogador inicia a mão.
        
        Args:
            jogador (Jogador): O jogador que abre a mão.
        """
        print(f"Jogador {jogador.nome} abre a mão!")

    def pergunta_truco(self, jogador_proponente: Jogador, valor: Ponto) -> bool:
        """
        Pergunta se um jogador deseja pedir truco.
        
        Para jogadores humanos, solicita uma entrada.
        Para jogadores máquina, decide aleatoriamente.
        
        Args:
            jogador_proponente (Jogador): O jogador a quem será feita a pergunta.
            valor (Ponto): O valor atual dos pontos da mão.
            
        Returns:
            bool: True se o jogador pediu truco, False caso contrário.
        """
        if jogador_proponente.tipo == TipoJogador.MAQUINA:
            escolha = rand()
            if escolha < .5:
                print(f"Jogador {jogador_proponente.nome} pediu {valor}!")
                return True
            else:
                return False
        else:
            resposta = input(f"Jogador {jogador_proponente.nome}, "
                            f"deseja pedir {valor}? (s/n) ").strip().lower()
            if resposta == 's':
                return True
            else:
                return False
        
    def informa_placar_jogo(self, jogador_A: Jogador, jogador_B: Jogador):
        """
        Exibe o placar geral do jogo.
        
        Args:
            jogador_A (Jogador): Primeiro jogador.
            jogador_B (Jogador): Segundo jogador.
        """
        print(f"Placar: {jogador_A.nome}: {jogador_A.pontos}, "
              f"{jogador_B.nome}: {jogador_B.pontos}")
        
    def informa_placar_mao(self, jogador_A: Jogador, jogador_B: Jogador, mao: Mao):
        """
        Exibe o placar da mão atual.
        
        Args:
            jogador_A (Jogador): Primeiro jogador.
            jogador_B (Jogador): Segundo jogador.
            mao (Mao): A mão atual do jogo.
        """
        vitorias_A, vitorias_B = mao.conta_vitorias()
        print(f"Placar da mão: {jogador_A.nome}: {vitorias_A}, "
              f"{jogador_B.nome}: {vitorias_B}")

    def informa_quem_correu(self, jogador: Jogador):
        """
        Informa qual jogador correu (desistiu da mão).
        
        Args:
            jogador (Jogador): O jogador que correu.
        """
        print(f"Jogador {jogador.nome} correu!")

    def mostra_mao(self, jogador: Jogador, mao: Mao):
        """
        Exibe as cartas na mão de um jogador.
        
        Args:
            jogador (Jogador): O jogador cuja mão será exibida.
            mao (Mao): A mão do jogo.
        """
        print(f"Mão do jogador {jogador.nome}:", end=" ")
        for i, carta in enumerate(mao.cartas_A):
            print(f"{carta.nome}", end=" ")
        print()

if __name__ == "__main__":
    """
    Código de teste executado apenas se este arquivo for rodado diretamente.
    """
    interface = Interface()
    baralho = Baralho("cartas.csv")
    mao = Mao()
    mao.coleta_cartas(baralho)
    jogador_A = Jogador("Jogador A")
    escolha = interface.escolhe_carta(jogador_A, mao.cartas_A)
    print(f"{jogador_A} escolheu a carta: {mao.cartas_A[escolha].nome}")