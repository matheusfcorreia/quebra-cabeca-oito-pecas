from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
  
  def adquirirPercepcao(self, percepcao_mundo):
    """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
    na tela para o usuário saber o que seu agente está percebendo.
    """
    tabuleiro = percepcao_mundo
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])

  def escolherProximaAcao(self):
    from acoes import AcaoJogador
    # try:
    i, j = (int(s) for s in input("Qual peça deseja mover (linhas, coluna)? ").split(',', 2))
    return AcaoJogador.mover(i, j)
    # except:
    #   return 'Valor inválido'
