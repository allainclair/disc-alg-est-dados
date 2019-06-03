## Árvores

![arvore](../images/arvore/arvore.svg)

[arvore](../images/arvore/arvore.svg)

* nó pai;
* nós filhos;
* **profundidade** de um dado nó é dado em relação ao nó raiz: a maior profundidade
  entre todos os nós nos da a **altura da árvore**;
* Um conjunto de nós com a mesma profundidade é denominado nível da árvore.

```Python tab=
class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.childs = []
```

### Árvore binária
 
* Cada nó (pai) tem **no máximo** 2 filhos (grau máximo 2). Ou seja, pode ter 0,
  1 ou 2 filhos;
* Os nós de uma árvore binária possuem graus zero, um ou dois. Um nó de grau zero é
  denominado folha.
  
```Python tab=
class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
```

### Árvore binária de busca (ABB)

Dado um nó N da ABB:

* Todos nós à esqueda de N são menores (ou iguais) à N;
* Todos nós à direita de N são maiores (ou iguais) à N.

![arvore](../images/arvore/bin-search-tree.svg)

[arvore](../images/arvore/bin-search-tree.svg)

#### Inserções

Para inserir um nó na ABB basta seguir as regras acima.

![insertion](../images/arvore/bst-isertion.svg)

[insertion](../images/arvore/bst-isertion.svg)

Nem sempre a árvore vai ficar "balanceada". Veremos formas de balancear árvores
mais a frente.


### Travessia em árvores

#### **IN**order

Processar: esquerda → raiz → direita.

![inorder](../images/arvore/tree-inorder.svg)

[inorder](../images/arvore/tree-inorder.svg)

Se a árvore for binária de busca, os elementos são mostrados em ordem crescente.

#### **PRE**order

Processar: raiz → esquerda → direita.

![preorder](../images/arvore/tree-preorder.svg)

[preorder](../images/arvore/tree-preorder.svg)

#### **POST**order:

Processar: esquerda → direita → raiz.

#### Remoção

* Se nó for folha: simples remoção;
* Se nó tiver um filho: coloca-se o filho no lugar do nó removido;
* Se nó tiver dois filhos: dado o nó *node* de remoção, buscar o maior de sua
  sub-árvore a esquerda e substituir no lugar de *node*.