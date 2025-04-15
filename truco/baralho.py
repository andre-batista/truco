import pandas as pd
from .carta import Carta

class Baralho:
    """
    Classe que representa um baralho de cartas para o jogo de Truco.
    A classe Baralho é responsável por carregar as cartas de um arquivo CSV e
    distribuí-las entre os jogadores.
    Attributes:
        cartas (pandas.DataFrame): DataFrame contendo as informações das cartas do baralho.
    Methods:
        distribui_cartas: Distribui um número específico de cartas para dois jogadores.
    """
    def __init__(self, arquivo_csv: str):
        """
        Inicializa a classe Baralho carregando as cartas de um arquivo CSV.

        Args:
            arquivo_csv (str): Caminho para o arquivo CSV contendo as informações das cartas.
        
        Attributes:
            cartas (pandas.DataFrame): DataFrame contendo as informações das cartas do baralho.
        """
        self.cartas = pd.read_csv(arquivo_csv)

    def distribui_cartas(self, num_cartas=3) -> list:
        """
        Distribui um número específico de cartas para dois jogadores.

        Args:
            num_cartas (int, optional): Número de cartas a serem distribuídas para cada jogador. 
                                        O padrão é 3.

        Returns:
            tuple: Uma tupla contendo duas listas:
                - jogador_A (list[Carta]): Lista de objetos `Carta` para o jogador A.
                - jogador_B (list[Carta]): Lista de objetos `Carta` para o jogador B.
        """
        cartas_escolhidas = self.cartas.sample(n=num_cartas*2)
        jogador_A = []
        jogador_B = []
        
        # Distribui as cartas para o jogador A
        for n in range(num_cartas):
            dados = cartas_escolhidas.iloc[n]
            carta = Carta(dados['Carta'], dados['Valor'])
            jogador_A.append(carta)
        
        # Distribui as cartas para o jogador B
        for n in range(num_cartas):
            dados = cartas_escolhidas.iloc[n+num_cartas]
            carta = Carta(dados['Carta'], dados['Valor'])
            jogador_B.append(carta)

        return jogador_A, jogador_B
    
if __name__ == "__main__":
    baralho = Baralho("cartas.csv")
    jogador_A, jogador_B = baralho.distribui_cartas()
    print("Jogador A:", [carta.nome for carta in jogador_A])
    print("Jogador B:", [carta.nome for carta in jogador_B])
