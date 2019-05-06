## [Alocação estática x dinâmica de memória](https://pt.wikipedia.org/wiki/Aloca%C3%A7%C3%A3o_de_mem%C3%B3ria)


## Lista

* [1, 1, 2, 3, 5, 8, 11, 21, 34, 55];
* ['joao', 'maria', 'jose'];
* [1.0, 2.1, 'maria', 10, 'joao'].

### Implementação

Formas de implementar listas.

#### Estática

A lista é previamente criada, logo seu tamanho é definido logo no começo.

![lista-estatica](../images/list/lista-estatica.svg)

```Python tab=
SIZE = 10
lista = [0]*SIZE
lista
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista[1] = 10
lista
[0, 10, 0, 0, 0, 0, 0, 0, 0, 0]
lista[5] = 20
lista
[0, 10, 0, 0, 0, 20, 0, 0, 0, 0]
```

#### Dinâmica

A lista pode ser iniciada sem elementos, e seu tamanho pode aumentar e diminuir
de acordo com a vontade do usuário da lista.

A lista dinâmica mais conhecida é a **lista ligada**.

![lista-dinamica](../images/list/lista-dinamica.svg)

```Python tab=
lista = []
lista
[]
lista.append(10)
lista
[10]
lista.append(11)
lista
[10, 11]
lista.insert(0, 12)
lista
[12, 10, 11]
```

## Operações em qualquer lista

* Criar lista;
* Adicionar;
* Ler;
* Modificar/Atualizar;
* Excluir;
* Excluir lista completa (usa-se o excluir).

```Python tab=
list_ = []  # Criar.
list_.append(10)  # Adicionar ao final.
list_.insert(0, 10)  # Adicionar 10 no indice 0.
a = list_[1]  # Ler.
list_[1] = 100   # Atualizar.
del list_[1]  # Excluir/Deletar pelo indice.
list_.remove(10)  # Excluir/Deletar valor.
del list_  # Excluir lista completa.
```

Exercício

* Dada duas listas, uma contendo **nomes**, e outra contendo **números de
  telefone**. Mantenha a lista consistente ao usar as operações de adicionar, ler, modificar e excluir;

* Para isso um usuário da aplicação pode adicionar nomes e números de telefones
  respectivos. Ou seja, adiciona-se primeiro um nome de pessoa para depois adicionar um numero dessa pessoa;

* O usuário pode buscar (ler) por nome o número da pessoa, e também pode buscar
  por telefone o nome da pessoa;

* Pode modificar e excluir também por nome ou número;

* Caso não encontre nome/número, mensagens devem indicar esses problemas ao   
  usuário da aplicação;

* O usuário pode pedir para mostrar toda a lista de telefones e nomes.

# Listas circulares "estáticas"

# Listas ligadas dinâmicas

## Listas duplamente ligadas

# Listas circulares dinâmicas
