from regras_abstratas import AbstractRegrasJogo;

class OitoPecas(AbstractRegrasJogo):
  def __init__(self):
    self.tabuleiro = [[0,1,2],[3,4,5],[6,7,8]]
    
  def registrarAgentePersonagem(self, personagem):
    """ Cria ou recupera id de um personagem agente.
    """
    return 1
    
  def isFim(self):
    """ Boolean indicando fim de jogo em True.
    """
    resultado = True
    if self.tabuleiro[0][0]!=0: resultado = False
    if self.tabuleiro[0][1]!=1: resultado = False
    if self.tabuleiro[0][2]!=2: resultado = False
    if self.tabuleiro[1][0]!=3: resultado = False
    if self.tabuleiro[1][1]!=4: resultado = False
    if self.tabuleiro[1][2]!=5: resultado = False
    if self.tabuleiro[2][0]!=6: resultado = False
    if self.tabuleiro[2][1]!=7: resultado = False
    if self.tabuleiro[2][2]!=8: resultado = False
    return resultado

  def gerarCampoVisao(self, id_agente):
    """ Retorna um EstadoJogoView para ser consumido por um agente
    específico. Objeto deve conter apenas descrição de elementos visíveis
    para este agente.

    EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
    sua manipulação direta não tem nenhum efeito no mundo de jogo real.
    """
    return self.tabuleiro

  def registrarProximaAcao(self, id_agente, acao):
    """ Informa ao jogo qual a ação de um jogador especificamente.
    Neste momento, o jogo ainda não é transformado em seu próximo estado,
    isso é feito no método de atualização do mundo.
    """
    self.acao_jogador = acao
  
  def atualizarEstado(self, diferencial_tempo):
    """ Apenas neste momento o jogo é atualizado para seu próximo estado
    de acordo com as ações de cada jogador registradas anteriormente.
    """
    from acoes import AcoesJogador
      if self.acao_jogador.tipo == AcoesJogador.MOVER:
        i, j = self.acao_jogador.parametros

        if self.elementos[i][j+1] = 0:
          self.elementos[i][j+1] = self.elementos[i][j]
          self.elementos[i][j] = 0

        elif self.elementos[i][j-1] = 0:
          self.elementos[i][j-1] = self.elementos[i][j]
          self.elementos[i][j] = 0

        elif self.elementos[i+1][j] = 0
          self.elementos[i+1][j] = self.elementos[i][j]
          self.elementos[i][j] = 0

        elif self.elementos[i-1][j] = 0
          self.elementos[i-1][j] = self.elementos[i][j]
          self.elementos[i][j] = 0
  
  def terminarJogo(self):
    """ Faz procedimentos de fim de jogo, como mostrar placar final,
    gravar resultados, etc...
    """
    print('Vencedor !!!')