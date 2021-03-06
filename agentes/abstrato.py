from abc import ABC, abstractmethod
class AgenteAbstrato(ABC):
  '''
  Classe abstrata de agentes artificiais racionais.
  '''

  @abstractmethod
  def adquirirPercepcao(self, percepcao_mundo):
    ''' Forma uma percepcao interna por meio de seus sensores, a partir das
    informacoes de um objeto de visao de mundo.
    '''
    return

  @abstractmethod
  def escolherProximaAcao(self):
    ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
    das percepções anteriores.
    '''
    return

def construir_agente(*args, **kwargs):
  """ Método factory para uma instância Agente arbitrária, de acordo com os
  paraâmetros. Pode-se mudar à vontade a assinatura do método.
  """
  from agentes.tipos import TiposAgentes
  from agentes.humano import AgentePrepostoESHumano
  from agentes.bfs import AgentePrepostoBfs
  from agentes.dfs import AgentePrepostoDfs
  from agentes.ids import AgentePrepostoIds
  from agentes.dls import AgentePrepostoDls
  from agentes.gulosa import AgentePrepostoGuloso
  from agentes.estrela import AgentePrepostoEstrela
  
  if args[0] == TiposAgentes.PREPOSTO_HUMANO:
    return AgentePrepostoESHumano()
  elif args[0] == TiposAgentes.AUTO_BFS:
    return AgentePrepostoBfs()
  elif args[0] == TiposAgentes.AUTO_DFS:
    return AgentePrepostoDfs()
  elif args[0] == TiposAgentes.AUTO_IDS:
    return AgentePrepostoIds()
  elif args[0] == TiposAgentes.AUTO_DLS:
    return AgentePrepostoDls()
  elif args[0] == TiposAgentes.AUTO_GULOSO:
    return AgentePrepostoGuloso()
  elif args[0] == TiposAgentes.AUTO_ESTRELA:
    return AgentePrepostoEstrela()
  else:
    raise NotImplementedError()
