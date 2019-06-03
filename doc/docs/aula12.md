## Aula de exercícios dia 2019-06-07 (sexta)

Tragam exercícios.

## Fila (*Queue*)

* Primeiro a entrar é primeiro a sair (*First in First out: FIFO*);

* Duas operações básicas: "enfileirar" e "desinfileirar" (*enqueue* e *dequeue*).

![remocoes](../images/stack-queue/queue.svg)


### Exercício

Considere uma pilha *p* vazia e uma fila *f* não vazia. Utilizando apenas os testes
de fila e pilha vazias, as operações Enfileira, Desenfileira, Empilha, Desempilha, e
uma variável *aux*, escreva uma função que inverta a ordem dos elementos da fila.


## Árvores

Estrutura de dado (TAD)

![arvore](../images/arvore/arvore.svg)

[arvore](../images/arvore/arvore.svg)

* nó pai;
* nós filhos.

```Python tab=
class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.childs = []
```

### Árvore binária

* Cada nó (pai) tem **no máximo** 2 filhos. Ou seja, pode ter 0, 1 ou 2.

#### Exemplo

```Python tab=
class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
```

### Árvore binária de busca (ABB)

Dado um nó N da árvore:

* Todos nós à esqueda de N são menores (ou iguais) à N;
* Todos nós à direita de N são maiores (ou iguais) à N.

![arvore](../images/arvore/bin-search-tree.svg)

[arvore](../images/arvore/bin-search-tree.svg)

Para inserir um nó na ABB basta seguir as regras acima

### Travessia em árvores

* **IN**order: esquerda, raiz, direita;
* **PRE**order: raiz, esquerda, direita;
* **POST**order: esquerda, direita, raiz.
