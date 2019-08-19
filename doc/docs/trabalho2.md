## Implementar Deque

* Filas (Queues) são estrutura de dados que respeitam a regra do primeiro elemento
  a entrar é o primeiro a sair (FIFO);
* Fila de Duas Pontas (Double ended queue), como o nome diz, a fila tem duas
  pontas: uma à direita e outra à esquerda;
* Para inserir e remover na ponta **direita** respectivamente: `dq.append(x); dq.pop();`
  igual a fila comum.
* Para inserir e remover na ponta **esquerda** respectivamente:
  `dq.appendleft(x); dq.popleft();`
* **O objetivo principal do trabalho é implementar uma Fila de Duas Pontas**
  (`class Deque`) com algumas restrições:

    * **Apenas pilhas** devem ser as estruturas de dados interna da `Deque` para
      manipular os itens inseridos (`append`) e removidos (`pop`), logo é
      necessário implementar a estrutura de dado "Pilha" (`Stack`). Use as pilhas
      implementadas em sala de aula se achar necessário.

* Caso a *Deque* esteja vazia, **`False` deve ser retornado**;

* **Nenhum módulo** (`import`) pode ser usado para o o trabalho, incluindo o módulo
  `collections` que serve de exemplo para mostrar como a Deque deve funcionar.

### Exemplo de funcionamento usando `collections.deque`

```pyhon
import collections
dq = collections.deque()

dq.append(10)
dq
deque([10])

dq.append(20)
dq.append(30)
dq.append(5)
dq
deque([10, 20, 30, 5])

dq.appendleft(50)
dq.appendleft(60)
dq.appendleft(70)
dq
deque([70, 60, 50, 10, 20, 30, 5])

dq.pop()
5
dq.pop()
30

dq.popleft()
70
dq.popleft()
60
dq.popleft()
50
dq.popleft()
10
dq.popleft()
20

dq.popleft()  # Ao inves do erro, retorne False na sua implementacao
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
```

## Entrega

* Entrega: 2019-09-08 23:59:59 - horário de recebimento;

* Entregar arquivo (anexo) **`main.py`** com **classe `Deque`** implementa;

* Enviar para **afsantos2@uem.br** com título (assunto): **T2 AED 7526 T31 - Nome1 RA1 - Nome2 RA2**;

* Até 2 membros;

* Cada dia de atraso desconta-se 10% da nota do trabalho total.
