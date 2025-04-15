from .mao import Mao
from .jogada import Vencedor
from .baralho import Baralho
from .jogador import Jogador, TipoJogador
from numpy.random import rand
from .jogada import Jogada
from .ponto import TipoPontos, Ponto
from .interface import Interface, TipoRespostaTruco


class Jogo:
    """
    Controla a lógica principal do jogo de truco.
    
    Esta classe é responsável por gerenciar o fluxo do jogo, incluindo a distribuição
    de cartas, controle de turnos, cálculo de pontuação, e verificação de condições de vitória.
    
    Atributos:
        interface (Interface): Objeto de interface para interação com os jogadores.
        
    Métodos:
        __init__(interface): Inicializa uma instância da classe Jogo.
        comecar(jogador_A, jogador_B, baralho): Inicia um novo jogo de truco.
        _verifica_fim_jogo(jogador_A, jogador_B): Verifica se o jogo terminou.
        _define_vencedor(jogador_A, jogador_B): Determina qual jogador venceu o jogo.
        _quem_abre_proxima(vencedor, ultima_rodada): Define quem abre a próxima rodada.
        _quem_abre_caso_correu(quem_correu): Define quem abre quando alguém correu.
        _propor_truco(jogador_proponente, jogador_resposta, valor): Gerencia pedidos de truco.
        _vez(jogador_vez, cartas_vez, jogador_espera, mao): Controla o turno de um jogador.
    """
    
    def __init__(self, interface: Interface):
        """
        Inicializa uma nova instância da classe Jogo.
        
        Args:
            interface (Interface): Objeto de interface para interação com os jogadores.
        """
        self.interface = interface
    
    def comecar(self, jogador_A: Jogador, jogador_B: Jogador, baralho: Baralho):
        """
        Inicia um novo jogo de truco.
        
        Configura os jogadores, distribui as cartas e gerencia o loop principal do jogo
        até que um jogador atinja a pontuação de vitória.
        
        Args:
            jogador_A (Jogador): Primeiro jogador.
            jogador_B (Jogador): Segundo jogador.
            baralho (Baralho): Baralho de cartas a ser usado no jogo.
        """
        jogador_A.iniciar_pontos()
        jogador_B.iniciar_pontos()
        jogador_A.adicionar_id(Vencedor.A)
        jogador_B.adicionar_id(Vencedor.B)
        fim_jogo = False
        
        # Sorteia quem começa o jogo
        if rand() < 0.5:
            jogador_que_abre = Vencedor.A
        else:
            jogador_que_abre = Vencedor.B
        
        # Loop principal do jogo
        while not fim_jogo:
            
            # Informa quem abre o jogo
            if jogador_que_abre == Vencedor.A:
                self.interface.informa_quem_abre(jogador_A)
            else:
                self.interface.informa_quem_abre(jogador_B)
            
            # Distribui as cartas
            mao = Mao()
            mao.coleta_cartas(baralho)
            
            # Loop da mão atual
            while not mao.mao_acabou():
                
                # Vez do jogador que abre
                if jogador_que_abre == Vencedor.A:
                    
                    escolha_A, mao, alguem_correu, quem_correu, valor = self._vez(
                        jogador_A, mao.cartas_A, jogador_B, mao
                    )  
                    
                elif jogador_que_abre == Vencedor.B:
                    
                    escolha_B, mao, alguem_correu, quem_correu, valor = self._vez(
                        jogador_B, mao.cartas_B, jogador_A, mao
                    )
                    
                # Verifica se alguém correu após o truco
                if alguem_correu:
                    jogador_que_abre = self._quem_abre_caso_correu(quem_correu)
                    break
                
                # Vez do outro jogador
                if jogador_que_abre == Vencedor.A:
                    
                    escolha_B, mao, alguem_correu, quem_correu, valor = self._vez(
                        jogador_B, mao.cartas_B, jogador_A, mao
                    )
                elif jogador_que_abre == Vencedor.B:
                    escolha_A, mao, alguem_correu, quem_correu, valor = self._vez(
                        jogador_A, mao.cartas_A, jogador_B, mao
                    )
                
                # Verifica se alguém correu após o truco
                if alguem_correu:
                    jogador_que_abre = self._quem_abre_caso_correu(quem_correu)
                    break
                
                # Compara as cartas para determinar o vencedor da jogada
                vencedor = mao.quem_ganhou_jogada(escolha_A, escolha_B)
                
                # Exibe o placar atual da mão
                self.interface.informa_placar_mao(jogador_A, jogador_B, mao)
                
                # Define quem abre a próxima rodada
                jogador_que_abre = self._quem_abre_proxima(vencedor,
                                                           jogador_que_abre)
                
                # Verifica se o jogo terminou
                fim_jogo = self._verifica_fim_jogo(jogador_A, jogador_B)
            
            # Finalização da mão atual
            if not alguem_correu:
                
                vencedor = mao.quem_ganhou_a_mao()
                
                # Atribui os pontos ao vencedor da mão
                if vencedor == Vencedor.A:
                    jogador_A.aumentar_pontos(mao.quanto_vale_a_mao())
                else:
                    jogador_B.aumentar_pontos(mao.quanto_vale_a_mao())
                    
            else:
                # Atribui os pontos quando alguém correu
                if quem_correu == jogador_A.id:
                    jogador_B.aumentar_pontos(valor)
                    vencedor = Vencedor.B
                else:
                    jogador_A.aumentar_pontos(valor)
                    vencedor = Vencedor.A
                    
            # Exibe o placar atual do jogo
            self.interface.informa_placar_jogo(jogador_A, jogador_B)
            
            # Verifica se o jogo terminou e exibe o vencedor
            if self._verifica_fim_jogo(jogador_A, jogador_B):
                vencedor = self._define_vencedor(jogador_A, jogador_B)
                self.interface.mostra_vencedor(vencedor)
                fim_jogo = True
    
    def _verifica_fim_jogo(self, jogador_A: Jogador,
                           jogador_B: Jogador) -> bool:
        """
        Verifica se o jogo terminou com base na pontuação dos jogadores.
        
        Args:
            jogador_A (Jogador): Primeiro jogador.
            jogador_B (Jogador): Segundo jogador.
            
        Returns:
            bool: True se algum jogador atingiu ou ultrapassou a pontuação de queda.
        """
        return (jogador_A.pontos >= TipoPontos.Queda.value
                or jogador_B.pontos >= TipoPontos.Queda.value)
    
    def _define_vencedor(self, jogador_A: Jogador,
                         jogador_B: Jogador) -> Jogador:
        """
        Determina qual jogador venceu o jogo.
        
        Args:
            jogador_A (Jogador): Primeiro jogador.
            jogador_B (Jogador): Segundo jogador.
            
        Returns:
            Jogador: O jogador com maior pontuação.
        """
        if jogador_A.pontos > jogador_B.pontos:
            return jogador_A
        elif jogador_B.pontos > jogador_A.pontos:
            return jogador_B
    
    def _quem_abre_proxima(self, vencedor: Vencedor,
                           ultima_rodada: Vencedor) -> Vencedor:
        """
        Define quem abre a próxima rodada.
        
        Args:
            vencedor (Vencedor): Vencedor da jogada atual.
            ultima_rodada (Vencedor): Jogador que abriu a rodada atual.
            
        Returns:
            Vencedor: Jogador que abrirá a próxima rodada.
        """
        if vencedor == Vencedor.A:
            return Vencedor.A
        elif vencedor == Vencedor.B:
            return Vencedor.B
        else:
            return ultima_rodada
    
    def _quem_abre_caso_correu(self, quem_correu: Vencedor) -> Vencedor:
        """
        Define quem abre a próxima rodada quando alguém correu.
        
        Args:
            quem_correu (Vencedor): Jogador que correu.
            
        Returns:
            Vencedor: Jogador que abrirá a próxima rodada.
        """
        if quem_correu == Vencedor.A:
            return Vencedor.B
        else:
            return Vencedor.A
    
    def _propor_truco(self, jogador_proponente: Jogador,
                      jogador_resposta: Jogador, valor: Ponto):
        """
        Gerencia o processo de propor e responder a pedidos de truco.
        
        Args:
            jogador_proponente (Jogador): Jogador que propõe o truco.
            jogador_resposta (Jogador): Jogador que responde ao pedido.
            valor (Ponto): Valor atual dos pontos da mão.
            
        Returns:
            tuple ou None: Uma tupla com (resposta, valor_atualizado, quem_correu) 
                          se houver pedido de truco, ou None caso contrário.
        """
        if self.interface.pergunta_truco(jogador_proponente, valor.proximo()):
            
            resposta, valor, quem_correu = self.interface.resposta_ao_truco(
                jogador_proponente, jogador_resposta, valor
            )
            return resposta, valor, quem_correu

        else:
            return None

    def _vez(self, jogador_vez: Jogador, cartas_vez: list, 
             jogador_espera: Jogador, mao: Mao):
        """
        Controla o turno de um jogador, incluindo proposta de truco e escolha de carta.
        
        Args:
            jogador_vez (Jogador): Jogador que está na vez.
            cartas_vez (list): Cartas disponíveis para o jogador.
            jogador_espera (Jogador): Jogador que está aguardando.
            mao (Mao): A mão atual do jogo.
            
        Returns:
            tuple: Uma tupla contendo (escolha, mao, alguem_correu, quem_correu, valor).
                escolha: Índice da carta escolhida.
                mao: Objeto Mao atualizado.
                alguem_correu: Boolean indicando se alguém correu.
                quem_correu: Vencedor indicando quem correu.
                valor: Ponto atual da mão.
        """
        alguem_correu = False
        quem_correu = None
        valor = None
        escolha = None
        
        # Mostra as cartas para jogadores humanos
        if jogador_vez.tipo == TipoJogador.HUMANO:
            self.interface.mostra_mao(jogador_vez, mao)
        
        # Verifica se pode propor truco (se não atingiu valor máximo)
        if not mao.mao_vale_queda():
            proposta = self._propor_truco(jogador_vez, jogador_espera,
                                          mao.pontos)
        
            if proposta is not None:
                resposta, valor, quem_correu = proposta

                if resposta == TipoRespostaTruco.ACEITAR:
                    mao.aumenta_pontos(valor)
                elif resposta == TipoRespostaTruco.CORRER:
                    alguem_correu = True                     
        
            # Se ninguém correu, escolhe uma carta
            if not alguem_correu:      
                escolha = self.interface.escolhe_carta(jogador_vez, cartas_vez)
        
        else:
            # Se já atingiu valor máximo, apenas escolhe uma carta
            escolha = self.interface.escolhe_carta(jogador_vez, cartas_vez)
        
        return escolha, mao, alguem_correu, quem_correu, valor