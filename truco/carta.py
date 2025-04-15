class Carta:
    """
    Representa uma carta de baralho com um nome e um valor associado.

    Atributos:
        nome (str): O nome da carta (ex.: "Ás de Espadas").
        valor (int): O valor numérico da carta, usado para comparações.

    Métodos:
        __init__(nome: str, valor: int):
            Inicializa uma instância da classe Carta com um nome e um valor.

        __str__() -> str:
            Retorna uma representação em string da carta (apenas o nome).

        __repr__() -> str:
            Retorna uma representação detalhada da carta para depuração.

        __eq__(outra) -> bool:
            Compara se duas cartas têm o mesmo valor.

        __lt__(outra) -> bool:
            Verifica se o valor da carta atual é menor que o valor de outra carta.

        __le__(outra) -> bool:
            Verifica se o valor da carta atual é menor ou igual ao valor de outra carta.

        __gt__(outra) -> bool:
            Verifica se o valor da carta atual é maior que o valor de outra carta.

        __ge__(outra) -> bool:
            Verifica se o valor da carta atual é maior ou igual ao valor de outra carta.
    """

    def __init__(self, nome: str, valor: int):
        """
        Inicializa uma instância da classe Carta.

        Args:
            nome (str): O nome da carta.
            valor (int): O valor numérico da carta.
        """
        self.nome = nome
        self.valor = valor

    def __str__(self) -> str:
        """
        Retorna uma representação em string da carta.

        Returns:
            str: O nome da carta.
        """
        return f"{self.nome}"

    def __repr__(self) -> str:
        """
        Retorna uma representação detalhada da carta para depuração.

        Returns:
            str: Uma string no formato "Carta(nome, valor)".
        """
        return f"Carta({self.nome}, {self.valor})"
    
    def __eq__(self, outra) -> bool:
        """
        Compara se duas cartas têm o mesmo valor.

        Args:
            outra (Carta): Outra instância de Carta para comparação.

        Returns:
            bool: True se os valores forem iguais, False caso contrário.
        """
        if isinstance(outra, Carta):
            return self.valor == outra.valor
        return False

    def __lt__(self, outra) -> bool:
        """
        Verifica se o valor da carta atual é menor que o valor de outra carta.

        Args:
            outra (Carta): Outra instância de Carta para comparação.

        Returns:
            bool: True se o valor da carta atual for menor, False caso contrário.
        """
        if isinstance(outra, Carta):
            return self.valor < outra.valor
        return False

    def __le__(self, outra) -> bool:
        """
        Verifica se o valor da carta atual é menor ou igual ao valor de outra carta.

        Args:
            outra (Carta): Outra instância de Carta para comparação.

        Returns:
            bool: True se o valor da carta atual for menor ou igual, False caso contrário.
        """
        if isinstance(outra, Carta):
            return self.valor <= outra.valor
        return False
    
    def __gt__(self, outra) -> bool:
        """
        Verifica se o valor da carta atual é maior que o valor de outra carta.

        Args:
            outra (Carta): Outra instância de Carta para comparação.

        Returns:
            bool: True se o valor da carta atual for maior, False caso contrário.
        """
        if isinstance(outra, Carta):
            return self.valor > outra.valor
        return False
    
    def __ge__(self, outra) -> bool:
        """
        Verifica se o valor da carta atual é maior ou igual ao valor de outra carta.

        Args:
            outra (Carta): Outra instância de Carta para comparação.

        Returns:
            bool: True se o valor da carta atual for maior ou igual, False caso contrário.
        """
        if isinstance(outra, Carta):
            return self.valor >= outra.valor
        return False