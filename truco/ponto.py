from enum import Enum

class TipoPontos(Enum):
    """
    Enumera os tipos de pontuação possíveis no jogo de truco.
    
    Valores:
        Comum (1): Pontuação para uma mão normal (1 ponto).
        Truco (3): Pontuação após pedido de truco (3 pontos).
        Seis (6): Pontuação após pedido de seis (6 pontos).
        Nove (9): Pontuação após pedido de nove (9 pontos).
        Queda (12): Pontuação máxima, após pedido de doze (12 pontos).
    """
    Comum = 1
    Truco = 3
    Seis = 6
    Nove = 9
    Queda = 12

class Ponto:
    """
    Representa a pontuação em uma mão do jogo de truco.
    
    Esta classe gerencia os valores de pontos em uma mão e oferece métodos
    para aumentar ou verificar a próxima pontuação possível.
    
    Atributos:
        valor (TipoPontos): O tipo atual da pontuação.
        
    Métodos:
        __init__(valor): Inicializa uma instância da classe Ponto.
        proximo(): Retorna o próximo nível de pontuação possível.
        aumenta(): Aumenta o nível de pontuação para o próximo valor.
        retorna_valor(): Retorna o valor numérico da pontuação atual.
        __str__(): Retorna uma representação em string do nível de pontuação.
    """
    
    def __init__(self, valor=TipoPontos.Comum):
        """
        Inicializa uma nova instância da classe Ponto.
        
        Args:
            valor (TipoPontos, opcional): O tipo inicial de pontuação. 
                                          Padrão é TipoPontos.Comum.
        """
        self.valor = valor

    def proximo(self):
        """
        Retorna o próximo nível de pontuação possível sem modificar o atual.
        
        Returns:
            Ponto: Um novo objeto Ponto com o próximo nível de pontuação.
        """
        if self.valor == TipoPontos.Comum:
            return Ponto(TipoPontos.Truco)
        elif self.valor == TipoPontos.Truco:
            return Ponto(TipoPontos.Seis)
        elif self.valor == TipoPontos.Seis:
            return Ponto(TipoPontos.Nove)
        elif self.valor == TipoPontos.Nove:
            return Ponto(TipoPontos.Queda)
        
    def aumenta(self):
        """
        Aumenta o nível de pontuação para o próximo valor.
        
        Modifica o valor do próprio objeto para o próximo nível de pontuação.
        """
        if self.valor == TipoPontos.Comum:
            self.valor = TipoPontos.Truco
        elif self.valor == TipoPontos.Truco:
            self.valor = TipoPontos.Seis
        elif self.valor == TipoPontos.Seis:
            self.valor = TipoPontos.Nove
        elif self.valor == TipoPontos.Nove:
            self.valor = TipoPontos.Queda

    def retorna_valor(self):
        """
        Retorna o valor numérico da pontuação atual.
        
        Returns:
            int: O valor numérico associado ao nível de pontuação atual.
        """
        return self.valor.value

    def __str__(self):
        """
        Retorna uma representação em string do nível de pontuação.
        
        Returns:
            str: Nome do nível de pontuação atual em texto.
        """
        if self.valor == TipoPontos.Comum:
            return "comum"
        elif self.valor == TipoPontos.Truco:
            return "truco"
        elif self.valor == TipoPontos.Seis:
            return "seis"
        elif self.valor == TipoPontos.Nove:
            return "nove"
        elif self.valor == TipoPontos.Queda:
            return "queda"

    def __eq__(self, outro) -> bool:
        """
        Compara se o valor atual é igual a outro valor.
        
        Args:
            outro (Ponto): O outro valor a ser comparado.
            
        Returns:
            bool: True se os valores forem iguais, False caso contrário.
        """
        return self.valor.value == outro.valor.value