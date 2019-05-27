## Início do 2º bimestre: Pilha e Fila

### Pilha (*Stack*)

* Primeiro a entrar é último a sair (*First in Last out: FILO*);

* Duas operações básicas: "empurrar" e "puxar" (*push* e *pop*).

![remocoes](../images/stack-queue/stack.svg)

#### Aplicação: Notação Sulfixo *Postfix*

##### Infixo:

`x ^ y / (5 * z) + 10`


##### Sufixo:

`x y ^ 5 z * / 10 +`

Usa-se uma pilha para criar a notação Sufixa (operador vem no final). Isto é,
dado operadores binários (dois argumentos), sempre que vier um número
(ou variável como no exemplo), empilha-se esses valores; já quando vier o operador,
desempilha-se os dois últimos elementos e aplica-se o operador, até que até que
seja consumido toda a lista que representa a operação completa.

**Dica:** usar função "eval" do Python para validar as expressões em formato de
string.

### Fila (*Queue*)

* Primeiro a entrar é primeiro a sair (*First in First out: FIFO*);

* Duas operações básicas: "enfileirar" e "desinfileirar" (*enqueue* e *dequeue*).

![remocoes](../images/stack-queue/queue.svg)
