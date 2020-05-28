#!/usr/bin/env python3

import time
from regras_jogo.regras_abstratas import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
  """ Se o jogo for em turnos, retorna a passada de 1 rodada.
  
  Se não for em turno, é continuo ou estratégico, retorna tempo
  preciso (ns) do relógio.
  """
  return 1 if em_turnos else time.time()


def iniciar_jogo():
  # Inicializar e configurar jogo
  mensagem = """Selecione o agente: \n 1) Humano \n 2) Bfs \n 3) Dfs
 4) Dls \n 5) Ids \n 6) Guloso \n 7) Estrela \n """
  agente_selecionado = input(mensagem)

  switcher = {
    1: TiposAgentes.PREPOSTO_HUMANO,
    2: TiposAgentes.AUTO_BFS,
    3: TiposAgentes.AUTO_DFS,
    4: TiposAgentes.AUTO_DLS,
    5: TiposAgentes.AUTO_IDS,
    6: TiposAgentes.AUTO_GULOSO,
    7: TiposAgentes.AUTO_ESTRELA
  }
  
  tipo_agente = switcher.get(int(agente_selecionado), 'Input inválido')
  
  jogo = construir_jogo(tipo_agente)
  personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
  agente_jogador = construir_agente(tipo_agente, Personagens.O_JOGADOR)
  
  tempo_de_jogo = 0
  while not jogo.isFim():
    # Mostrar mundo ao jogador
    ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
    agente_jogador.adquirirPercepcao(ambiente_perceptivel)
    
    # Decidir jogada e apresentar ao jogo
    acao = agente_jogador.escolherProximaAcao()
    if (acao == 'Valor inválido'):
      print(acao)
    else:
      jogo.registrarProximaAcao(personagem_jogador, acao)

      # Atualizar jogo
      tempo_corrente = ler_tempo()
      jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
      tempo_de_jogo += tempo_corrente
  
  jogo.terminarJogo();

if __name__ == '__main__':
    iniciar_jogo()