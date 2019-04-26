## Recursão

* Função chama ela própria no seu escopo;

* Para isso é necessário uma "condição base";

* Chamadas vão sendo empilhadas e depois desempilhadas ao passo que se chega na
  "condição base" e assim a última chamada retorna algum valor;

* Muitos algoritmos (todos os iterativos) podem ter uma versão recursiva.

### Exemplos

* soma de lista;

* exponencial;

* fatorial.


## Pesquisa sequencial

Dado um elemento, e uma lista, encontre o elemento dentro dessa lista e retorne
vedadeiro se encontrar; falso caso contrário.

## Pesquisa binária

* Requisito: lista ordenada;

## [Alocação estática x dinâmica de memória](https://pt.wikipedia.org/wiki/Aloca%C3%A7%C3%A3o_de_mem%C3%B3ria)

### Memória RAM

Um vetor de caracteres armazenados em memória RAM.

```
# Assumindo que cada caracter tem um byte.

vetor = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

Endereço  Dado

100000    '1'
100001    '2'
100002    '3'
100003    '4'
100004    '5'
100005    '6'
100006    '7'
100007    '8'
100008    '9'
100009    '10'
```
