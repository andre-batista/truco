"""
Truco - Uma biblioteca Python para o jogo de truco.
"""

__version__ = "0.1.0"
__author__ = "Andre"

# Importa os componentes principais para torná-los disponíveis ao 
# importar o pacote
from .baralho import Baralho
from .jogador import Jogador
from .jogo import Jogo
from .interface import Interface

# A variável __all__ define especificamente quais nomes serão importados 
# quando alguém usar a sintaxe: from truco import *
# Neste caso, apenas quatro classes ou módulos serão importados: Baralho,
# Jogador, Jogo e Interface. Isso é uma boa prática porque:
# * Limita o que é exposto ao namespace global do usuário
# * Torna explícito quais são os componentes principais do pacote
# * Evita a importação acidental de módulos auxiliares ou internos
# Sem esta definição, from truco import * importaria todos os nomes 
# disponíveis no pacote, o que poderia causar poluição do namespace e 
# possíveis conflitos de nomes.
__all__ = [
    "Baralho",
    "Jogador",
    "Jogo",
    "Interface"
]