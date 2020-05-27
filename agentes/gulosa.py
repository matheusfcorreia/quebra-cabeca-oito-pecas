from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
from copy import deepcopy

class AgentePrepostoGuloso(AgenteAbstrato):
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
    resultado = [True, 0]
    if estado[0][0]!=0: 
      resultado[0] = False 
      resultado[1] = resultado[1] + 1
    if estado[0][2]!=2: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][0]!=3: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][1]!=4: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][2]!=5: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][0]!=6: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][1]!=7: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][2]!=8: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    
    return resultado

  def adquirirPercepcao(self, percepcao_mundo):
    """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
    na tela para o usuário saber o que seu agente está percebendo.
    """
    self.opcoes = percepcao_mundo.opcoes
    self.borda = percepcao_mundo.borda
    self.percorridos = percepcao_mundo.percorridos
    self.tabuleiro = percepcao_mundo.tabuleiro
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

  def buscaGulosa(self, borda, tabuleiro, percorridos, caminho):
    borda.insert(0, tabuleiro) 
    #Verifica se o jogo ja foi resolvido
    if not self.resolvido:
      #Percorre todos estados da borda até encontrar o estado final
      menos_pecas_fora = 9
      while len(borda) > 0:
        estado_temp = False
        fim = False

        # Seleção do estado a ser buscado pela sua diminuição de elementos fora do lugar
        if len(borda) == 1: estado_temp = borda.pop(0)
        else:
          for i in range(len(borda)-1):
            fim = self.isFim(borda[i])
            if fim[1] < menos_pecas_fora: 
              menos_pecas_fora = fim[1]
              estado_temp = borda.pop(i)
            
          if estado_temp == False:
            estado_temp = borda.pop(0) 
            for i in range(len(borda)-1):
              fim = self.isFim(borda[i])
              if self.isFim(estado_temp)[1] < fim[1]:
                estado_temp = borda.pop(i) 

        #Limpa a borda para a seleção do próximo elemento mais saboroso       
        borda.clear()
        percorridos.append(estado_temp)
        if self.isFim(estado_temp)[0] == True: 
          self.resolvido = True
          print('Resolvi o puzzle!')
          print('Tentativas: ', len(self.jogadas))
          # Uni as referências até o estado final na variável caminho
          tabuleiro.pop(3)
          return self.gerarCaminho(tabuleiro, caminho, percorridos)
          
          break
        #Se não for o estado final, gera os estados filhos e os adiciona ao início borda
        else: 
          filhos = [
            self.gerarEstados(opcao, estado_temp, False) for opcao in self.validarOpcoes(estado_temp)
          ]

          for filho in filhos:
            borda.insert(0, filho)


  def escolherProximaAcao(self):
    if not self.resolvido:
      self.caminho = self.buscaGulosa(self.borda, self.tabuleiro, self.percorridos, self.caminho)
    
    acao = AcaoJogador.mover(self.caminho[0][3][0], self.caminho[0][3][1])
    self.caminho.pop(0)
    return acao
