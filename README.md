# 8 Puzzle - Projeto Inteligencia Artificial

Projeto desenvolvido na disciplina de Inteligencia Artificial, onde o jogo 8 Puzzle foi implementado junto com algumas aplicações de métodos de busca e agentes inteligentes para a resolução do jogo. 

### > **Linguagem Representativa** 
Estado inicial: OitoPecas([[5, 6, vazio], [8, 4, 7], [2, 3, 1]]);  
(Sendo vazio = 0)

Objetivo: OitoPecas([[vazio, 1, 2], [3, 4, 5], [6, 7, 8]]);

Ações: Mover([linha, coluna]); 

#### Exemplo de Aplicação da Linguagem

Ações(OitoPecas([[1, 4, 2], [3, 5, vazio], [6, 7, 8]])) -> 
Mover([1, 1]) -> OitoPecas([[1, 4, 2], [3, vazio, 5], [6, 7, 8]])
Mover([0, 1]) -> OitoPecas([[1, vazio, 2], [3, 4, 5], [6, 7, 8]])
Mover([0, 0]) -> OitoPecas([[vazio, 1, 2], [3, 4, 5], [6, 7, 8]])

![Exemplo Visual](/assets/exemplo.png)

#### Descrição das Ações

Única ação é a MOVER. Está ação recebe a posição do elemento que o jogador deseja movimentar, sempre verificando se é uma ação válida, ou seja, verifica se a peça selecionada pode ser movimentada de acordo com as regras do jogo.

Mover([linha, coluna]); 

Sendo linha e coluna referentes a posição do elemento a ser movido (valores de linhas e colunas baseados em posições de elementos em listas da linguagem python).

**Resultados de Ações na Prática**
![Resultados de Ações na Prática](/assets/estados.png)

**Exemplo de Árvore até o Objetivo**
![Exemplo de Árvore até o Objetivo](/assets/arvore.png)

### > **Heurística do Problema** 

Como avaliação heurística, foi escolhido o sistema de contagem de peças fora de sua posição, sendo avaliado, antes de cada ação, se aquele movimento diminuiria ou não a quantidade de peças fora do lugar. Sendo assim:
  - AvaliarMovimento(estado_pós_movimento) -> retorna quantidade de peças fora de posição;

Em casos que não há uma diminuição visível no número de peças fora de posição, o algorítmo de escolher uma ação aleatoriamente, evitando estados já percorridos.

#### Avaliação da Heurística

Apesar de ser uma heurística bem simples, é totalmente válida e consistente, por conta da busca direta pelo posicionamento ideal das peças. Combinada com um algorítmo de busca com memória, torna-se uma estratégia bem viável, evitando loopings e indo direto ao ponto final desejado, diminuindo o deperdício de recursos na aberto de estados desnecessários.


### > **Diagramas**

**Diagrama de Pacotes**               
![Diagrama de Pacotes](/assets/pacotes.png)

**Diagrama de Classes**          
![Diagrama de Classes](/assets/classes.png)

**Diagrama de Sequencia**            
![Diagrama de Sequencia](/assets/sequencia.png)
