## Classes e Objetos

```Python tab=
class Name:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
    
    def method1(self, attr):
        self.attr1 += attr
    
    def method2(self, attr):
        self.attr2 += attr


name = Name(1, 2)
name.attr1
1
name.attr2
2

name.method1(2)
name.attr1
3

name.method2(2)
name.attr2
4


class Pessoa:
    pass
```

## Listas

```Python tab=
indices = [0, 1, 2, 3, 4, 5,  6,  7]
list_ =   [1, 1, 2, 3, 5, 8, 11, 21]
```

### Listas ligadas

Esse tipo de listas **não são acessadas por índices**, apenas é possível "caminhar"
pela lista para manipular elas, ou seja, para ler, adicionar, modificar e excluir
elementos da lista ligada.

![linked-list](../images/list/linked-list.svg)

#### Listas ligadas estáticas

Usa-se estruturas de dados "comuns" estáticas como vetores. No Python usamos
o a estrutura lista (*list*).

#### Listas ligadas dinâmicas

Usa-se "registros recursivos" (estrutura de dado recursiva) para ligar os nós
da lista. 

#### Listas duplamente ligadas (dinâmicas)

Na estrutura de dado nó, adicionamos outro apontador para o elemento anterior.

## Listas circulares

![circular-list](../images/list/circular-list.svg)

### Listas circulares "estáticas"

### Listas circulares dinâmicas duplamente ligadas