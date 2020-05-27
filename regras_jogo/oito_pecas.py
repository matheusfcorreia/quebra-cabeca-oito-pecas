from regras_jogo.regras_abstratas import AbstractRegrasJogo;

class OitoPecas(AbstractRegrasJogo):
  def __init__(self):
    self.tabuleiro = [[1,4,2],[3,5,0],[6,7,8],[]]
    self.opcoes = []
    self.borda = []
    self.percorridos = []
    self.tentativas = 0
    self.profundidade = input('Qual a profundidade máxima?  ')
    # self.tabuleiro = [[6,2,7],[4,0,5],[8,1,3],[]]
    
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
    game = self
    return game

  def registrarProximaAcao(self, id_agente, acao):
    """ Informa ao jogo qual a ação de um jogador especificamente.
    Neste momento, o jogo ainda não é transformado em seu próximo estado,
    isso é feito no método de atualização do mundo.
    """
    i, j = acao.parametros
    mensagem_erro = 'Ação Inválida'

    if i > 3 or i < 0:
      if j > 3 or j < 0:
        acao = mensagem_erro
      acao = mensagem_erro

    self.acao_jogador = acao
  
  def atualizarEstado(self, diferencial_tempo):
    """ Apenas neste momento o jogo é atualizado para seu próximo estado
    de acordo com as ações de cada jogador registradas anteriormente.
    """
    from acoes import AcoesJogador
    mensagem_erro = 'Ação Inválida'
    
    if self.acao_jogador == 'Ação Inválida':
      print(mensagem_erro) 
    else:
      if self.acao_jogador.tipo == AcoesJogador.MOVER:
        i, j = self.acao_jogador.parametros

        if j+1 <= 2:
          if self.tabuleiro[i][j+1] == 0:
            self.tabuleiro[i][j+1] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = 0
            
        elif j-1 >= 0:
          if self.tabuleiro[i][j-1] == 0:
            self.tabuleiro[i][j-1] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = 0
            
        else:
          print(mensagem_erro)
          
        
        if i+1 <= 2:
          if self.tabuleiro[i+1][j] == 0:
            self.tabuleiro[i+1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = 0
            
        elif i-1 >= 0:
          if self.tabuleiro[i-1][j] == 0:
            self.tabuleiro[i-1][j] = self.tabuleiro[i][j]
            self.tabuleiro[i][j] = 0
            
        else: 
          print(mensagem_erro) 
    
  
  def terminarJogo(self):
    """ Faz procedimentos de fim de jogo, como mostrar placar final,
    gravar resultados, etc...
    """
    print(self.tabuleiro[0])
    print(self.tabuleiro[1])
    print(self.tabuleiro[2])
    print('Vencedor !!!')