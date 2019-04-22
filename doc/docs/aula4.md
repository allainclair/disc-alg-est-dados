## Exercício: encontrar posição de um elemento em um vetor **

Dado uma `lista` (vetor) e um `elemento` como entrada para uma função chamda
de `find`, retorne a posição do elemento encontrado; caso não seja 
encontrado retorne `None` (nulo).

```Python tab=
def find(list_, element)
```

### Pesquisa sequencial

Dado um elemento, e uma lista, encontre o elemento dentro da lista sem usar 
o operado `in`.

## Pesquisa binária

* Requisito: lista ordenada;

## Exemplos e revisão

### Vetor (Arranjo)

#### Formato:

```Python tab=
# Em python o nome dessa estrutura de dado eh conhecida como lista
# Mas para fins de exemplo criamos uma variavel com o nome vetor.
# Indices do vetor comeca em 0.
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vetor[0])
1
```

```C tab=
/* Aqui alocamos um vetor de inteiros com 10 elementos, sendo eles todo 
*  o intervalo [1, 10].
*  Indicies comecam em 0.
*/ 
int vetor[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
printf("%d", vetor[0]);
1
```

#### Gerenciamento:

Em um vetor podemos: **adicionar, atualizar, excluir e ler** elementos.

##### Adicionar *

Adição modifica o vetor original, aumentando pelo menos um elemento novo.

```Python tab=
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor.append(11)  # Metodo (funcao) de orientacao a objeto.
vetor
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Apenas para mostrar como eh no "paradigma estrutural".
def meu_append(vetor, novo_elemento):
    vetor.append(novo_elemento)
    # Funcao nao retorna nada, podemos chamar de "procedimento".

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
meu_append(vetor, novo_elemento)
vetor
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 

```

##### Atualizar *

Atualização precisa modificar algum elemento já existente do vetor original.

```Python tab=
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor[2] = 11
vetor
[1, 2, 11, 4, 5, 6, 7, 8, 9, 10]
```

##### Remover *

```Python tab=
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor.remove(5)  # Qual algoritmo eh necessario ANTES de remover?
vetor
[1, 2, 3, 4, 6, 7, 8, 9, 10]
# TODO: exercicio: fazer o seu proprio remover.
def meu_remover(vetor, elemento):
    pass
    # Funcao nao retorna nada
```

##### Ler *

```Python tab=
# Leitura NAO pode modificar o nosso vetor original
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = vetor[2]
a
2
# Leitura direta do vetor para impressao
print(vetor[2])
```

#### Armazenamento: **

Memória RAM, registradores do processador (CPU), dispositivo de 
armazenamento secundário (HDDs, SSDs, etc).

##### Memória RAM **

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
