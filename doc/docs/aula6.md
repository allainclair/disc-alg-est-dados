## Pesquisa sequencial

Dado um elemento, e uma lista, encontre o elemento dentro dessa lista e retorne
vedadeiro se encontrar; falso caso contrário.

Ex: Implementar tipo o método "count()". Ou seja, contar quantas vezes o elemento "element" está na lista "list_".

```Python tab=
def count(list_, element):
    return "count"
```

## Pesquisa binária

* Requisito: lista ordenada;

* Algoritmo iterativo;

* Algoritmo recursivo.

Implementar o "count()" usando pesquisa binária. Lembrando que para usar a pesquisa binária a lista precisa estar ordenada.

## Pesquisa através de cálculo de endereço

* Hash;

* f(elemento) -> endereço.

* Adicionamos esse elemento no endereço, e buscamos esse elemento por meio
  novamente de f(elemento);

* Para inserir e para buscar o elmenento as operação são em tempo constante
  ("1 acesso");

* Existe um mapeamento do elemento para um número (um endereço), e esse endereço nos
  retorna o elemento quando ele é buscado;

* Dicionário d = {1: 10, 2: 5, 'joao': [1, 2, 3]}.

## [Alocação estática x dinâmica de memória](https://pt.wikipedia.org/wiki/Aloca%C3%A7%C3%A3o_de_mem%C3%B3ria)
