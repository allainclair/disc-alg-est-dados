## Remoção em ABB

* Remoção de nó folha;

* Remoção de nó com filhos:

    * Se tiver apenas um filho. Coloca-se o filho no lugar;

    * Com nós que tem dois filhos: troca-se pelo imediatamente maior ou pelo
      imediatamente menor.


### Exemplo

![remocao](../images/arvore/remocao.svg)

## Árovre AVL (**A**delson-**V**elsky and **L**andis)

* Uma árvore binária que tem por objetivo manter a árvore balanceada. Ou seja,
  que não tenham desníveis exagerados;

* Quando a diferença de nível das sub-árvores (esquerda e direita) de um dado nó  
  for maior do que 1, é necessário rotacionar.

## Propriedade

Para cada nó da Árvore AVL, suas sub-árvores (esquerda e direita) tem uma
diferença de níveis de no máximo 1.

* A = conjunto de nós da árvore;

* h(x) = altura de um nó x;

* fesq(x) = filho à esquerda de x;

* fdir(x) = filho à direita de x;

* ∀x ∈ A, |h(fesq(x)) - h(fdir(x))| ≤ 1.

### Exemplos balanceamento

![remocao](../images/arvore/avl1.svg)

Balanceada

![remocao](../images/arvore/abb-nao-balanceada-1.svg)

Não balanceada

### Balanceamento

Rotacionamento de árvore: rotação à direita e à esquerda.

* Rotação à direita:

![left-case](../images/arvore/left-case.png)

* Rotação à esquerda:

![right-case](../images/arvore/right-case.png)

* Rotação dupla: esquera e direita:

![left-right-case](../images/arvore/left-right-case.png)

* Rotação dupla: direita e esquerda:

![right-left-case](../images/arvore/right-left-case.png)
