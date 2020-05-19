from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
  MOVER = 'mover'

@dataclass
class AcaoJogador():
  tipo: str
  parametros: tuple = tuple()

  @classmethod
  def mover(cls, i, j):
    return cls(AcoesJogador.MOVER, (i,j))
    