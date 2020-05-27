from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
from copy import deepcopy

class AgentePrepostoDls(AgenteAbstrato):
  resolvido = False
  jogadas = []
  caminho = [[[0,1,2],[3,4,5],[6,7,8]]]
  def validarOpcoes(self, tabuleiro):
    opcoes = []
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        if tabuleiro[i][j] == 0:
          if i+1 < 3: opcoes.append([i+1,j])
          if i-1 > -1: opcoes.append([i-1,j])

          if j+1 < 3: opcoes.append([i,j+1])
          if j-1 > -1: opcoes.append([i,j-1])
    
    return opcoes

  def gerarEstados(self, opcao, tabuleiro, valendo):
    i, j = opcao
    tabuleiro_aux = deepcopy(tabuleiro)
    tabuleiro_aux2 = deepcopy(tabuleiro)
    
    if i+1 <= 2:
      if tabuleiro_aux[i+1][j] == 0:
        tabuleiro_aux[i+1][j] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0
        
    elif i-1 >= 0:
      if tabuleiro_aux[i-1][j] == 0:
        tabuleiro_aux[i-1][j] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0

    if j+1 <= 2:
      if tabuleiro_aux[i][j+1] == 0:
        tabuleiro_aux[i][j+1] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0
        
    elif j-1 >= 0:
      if tabuleiro_aux[i][j-1] == 0:
        tabuleiro_aux[i][j-1] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0

    if tabuleiro_aux not in self.percorridos: self.jogadas.append(opcao)
    
    if valendo == False: 
      tabuleiro_aux[3] = [tabuleiro_aux2[0], tabuleiro_aux2[1], tabuleiro_aux2[2], opcao]

    return tabuleiro_aux
    
  def isFim(self, estado):
    """ Boolean indicando fim de jogo em True.
    """
    resultado = True
    if estado[0][0]!=0: resultado = False
    if estado[0][1]!=1: resultado = False
    if estado[0][2]!=2: resultado = False
    if estado[1][0]!=3: resultado = False
    if estado[1][1]!=4: resultado = False
    if estado[1][2]!=5: resultado = False
    if estado[2][0]!=6: resultado = False
    if estado[2][1]!=7: resultado = False
    if estado[2][2]!=8: resultado = False
    # if resultado is True: print(estado)
    return resultado

  def adquirirPercepcao(self, percepcao_mundo):
    """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
    na tela para o usuário saber o que seu agente está percebendo.
    """
    self.opcoes = percepcao_mundo.opcoes
    self.borda = percepcao_mundo.borda
    self.percorridos = percepcao_mundo.percorridos
    self.tabuleiro = percepcao_mundo.tabuleiro
    self.profundidade = percepcao_mundo.profundidade
    self.tentativas = percepcao_mundo.tentativas + 1
    
    print('jogada')
    print(percepcao_mundo.tabuleiro[0])
    print(percepcao_mundo.tabuleiro[1])
    print(percepcao_mundo.tabuleiro[2])
    
    print('\n')

  def gerarCaminho(self, tabuleiro, caminho, percorridos):
    caminho_aux =  deepcopy(caminho)
    while caminho_aux[0][:3] != tabuleiro:
      ult_percorrido = percorridos[-1]

      if self.isFim(ult_percorrido[:3]) == True:
        caminho_aux.insert(0,ult_percorrido[3])
        
      else:
        for percorrido in percorridos:
          if percorrido[:3] == caminho_aux[0][:3]:
            if percorrido[:3] is not caminho_aux: caminho_aux.insert(0, percorrido[3])

      percorridos.pop(-1)
    return caminho_aux

  def escolherProximaAcao(self):
    self.borda.insert(0, [self.tabuleiro, 0]) 
    
    altura = 0
    #Verifica se o jogo ja foi resolvido
    if self.resolvido is False:
      #Percorre todos estados da borda até encontrar o estado final
      while len(self.borda) > 0:
        #Verifica se a altura do estado aberto está dentro do padrão exigido
        if self.borda[0][1] <= int(self.profundidade):
          altura = self.borda[0][1] 
          estado_temp = self.borda.pop(0)[0]
        else: 
          self.borda.pop(0)
          altura = self.borda[0][1]
          estado_temp = self.borda.pop(0)[0]

        self.percorridos.append(estado_temp)
        if self.isFim(estado_temp) == True: 
          self.resolvido = True
          print('Resolvi o puzzle!')
          print('Tentativas: ', len(self.jogadas))
          # Uni as referências até o estado final na variável caminho
          self.tabuleiro.pop(3)
          self.caminho = self.gerarCaminho(self.tabuleiro, self.caminho, self.percorridos)
          
          break
        #Se não for o estado final, gera os estados filhos e os adiciona ao início borda
        else: 
          filhos = [
            self.gerarEstados(opcao, estado_temp, False) for opcao in self.validarOpcoes(estado_temp)
          ]

          for filho in filhos:
            ja_percorrido = False
            for percorrido in self.percorridos:
              if filho[:3] == percorrido[:3]: ja_percorrido = True
            if ja_percorrido == False: 
              self.borda.insert(0, [filho, altura])
              altura = altura + 1

    acao = AcaoJogador.mover(self.caminho[0][3][0], self.caminho[0][3][1])
    self.caminho.pop(0)
    return acao
