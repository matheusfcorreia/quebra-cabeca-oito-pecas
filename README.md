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

Única ação é a MOVER

Mover([linha, coluna]); 

Sendo linha e coluna referentes a posição do elemento a ser movido (valores de linhas e colunas baseados em posições de elementos em listas da linguagem python).

**Resultados de Ações na Prática**
![Resultados de Ações na Prática](/assets/estados.png)

**Exemplo de Árvore até o Objetivo**
![Exemplo de Árvore até o Objetivo](/assets/arvore.png)
