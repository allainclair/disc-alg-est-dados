## Exercício 1.1

Defina uma função chamada `max3` que dado 3 números (a, b, c) ela retorne o 
maior entre eles (sem usar a função `max()`).


```Python tab=
# Para testar seu codigo adicione esses codigos no seu arquivo.
retorno = max3(1, 2, 3)
print('Apenas o primeiro retorno:', retorno)
assert retorno == 3
assert max3(4, 2, 3) == 4
assert max3(4, 5, 3) == 5
assert max3(10, 5, 3) == 10
assert max3(10, 5, 11) == 11
print('Tudo certo!!?')
```
## Exercício 1.2

Faça um função chamada `media_pond3` que leia as 3 notas de um aluno e 
retorne a média final deste aluno. Considerar que a média é ponderada e que o
 peso das notas é: 1, 2 e 3 respectivamente.

```Python tab=
# Para testar seu codigo adicione esses codigos no seu arquivo.
# Necessario mais testes!
retorno = media_pond3(10, 10, 10)
print('Apenas o primeiro retorno:', retorno)
assert retorno == 10
assert media_pond3(2, 2, 6) == 4
print('Tudo certo!!?')
```

### Exercício 1.2.1

Faça uma função chamada `aprovar` que retorne Verdadeiro (`True`) ou Falso 
(`False`) caso o aluno seja aprovado ou reprovado respectivamente, com as 
mesmas regras do Exercício 1.2. Funções que só retornam `True` ou `False` são chamadas de **funções booleanas**.

Imprima 'Aprovado' ou 'Reprovado' dentro da função. Para um aluno ser 
aprovado é necessário que ele tenha no mínimo 6 de nota. É completamente válido
reusar o código do Exercício 1.2.

```Python tab=
# Sem testes ainda!
```


## Exercício 1.3

Construa uma função `dist()` que, tendo como dados de entrada dois 
pontos quaisquer no plano, p(x1,y1) e p(x2,y2), retorne a distância entre 
eles. A ordem dos parâmetros são: x1, y1, x2 e y2.

```Python tab=
# Faca mais testes se voce quiser mais garantia
# Preste a atencao na quantidade de parametros e seus respectivos nomes. 
retorno = dist(0, 0, 0, 1)
print('Apenas o primeiro retorno:', retorno)
assert retorno == 1
assert dist(0, 0, 1, 0) == 1
assert dist(0, 0, 2, 0) == 2
assert dist(0, 0, 0, 3) == 3
assert dist(1, 1, 2, 1) == 1
print('Tudo certo!!?')
```

## Exercício 1.4

Faça um programa para ler o salário de um funcionário e aumentá-lo em 15%.
Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário
com o aumento e o salário final.

### Exercício 1.4.1

Transforme o programa em uma função `salario_liquido`, que recebe o salário 
como argumento e retorne o salário líquido com as regras do exercódio 1.3.


## Exercício 1.5

Elabore um programa que dada a idade de um nadador classifica-o em uma das 
seguintes categorias:
 
* `Infantil A` = 5-7 anos

* `Infantil B` = 8-10 anos

* `Juvenil A` = 11-13 anos

* `Juvenil B` = 14-17 anos

* `Adulto` = maiores de 18 anos

Também transforme seu programa em uma função, caso não o tenha feito. Ou 
seja, sua função terá como parâmetro a idade do nadador e retorna uma string
 com o nome da categoria do nadador
 
## Exercício 1.6

Escreva um programa para contar dinheiro que pergunte, dentro de um monte de
dinheiro, qual a quantidade de notas de:

* 1 real;
* 2 reais;
* 5 reais;
* 10 reais;
* 50 reais;
* 100 reais.

Em seguida programa imprime qual o valor total em dinheiro.

Exemplo: 2 notas de 1 real e 5 notas de 100 reais (entrada) dão um total de 
502 reais (saída). 

## Exercício 1.7 

Escreva um programa que faça o inverso da questão anterior, ou seja, solicite
ao usuário um valor (total) em dinheiro, e informe quantas notas de: 1 real,
2 reais, 5 reais, 10 reais, 50 reais e 100 reais serão necessárias para compor
este valor, de forma que seja utilizado o menor número de notas possível.

**Exemplo:** 507 reais são 5 notas de  100 reais, 1 nota de 5 reais e 2 notas
de 1 real.

**Bonus:** minimize a quantidade de notas. No exemplo anterior poderia-se usar 
1 nota de 2 reais ao invés de 2 notas de 1 real.
  

## Exercício 1.8

  
Uma agencia de espionagem encomendou um programa especial para fazer a codificação
de mensagens. O programa inicialmente lê a mensagem e codifica da seguinte forma:

* Considerando os caracteres que compõem a mensagem aos pares, cada caractere é
  trocado com o seu vizinho, sempre levando em consideração que isto é feito
  aos pares,como mostra o exemplo abaixo:
  
**mensagem original:** 'Esta é uma mensagem.';

**processo codificação:** 'E s t a _ é _ u m a _ m e n s a g e m .'; (caracteres
  _ indicam os espaços em branco)

**mensagem codificada:** 'sEaté u amm neaseg.m';

* Se o número de caracteres for ímpar, o programa acrescenta um caractere '#' 
no final **antes** de realizar a troca dos pares.

## Exercício 1.9

Considere o código abaixo e responda as questões:

```Python
if b1 == True:
    c1 = True
else:
     if b2 == True:
         if b3 == True:
             c2 = True
         else:
             c3 = True
        c4 = True
c5 = True
```

1. Se b1 = `True` , b2 = `True` e b3 = `False`, quais comandos serão executados
   pelo algoritmo?

2. Se b1 = `False`, b2 = `True` e b3 = `False`, quais comandos serão executados?

3. Se b1 = `False`, b2 = `True` e b3 = `True`, quais comandos serão executados?

4. Quais valores lógicos b1, b2 e b3 devem receber para que somente o comando
`c5` seja executado? 

## Fontes:

* [https://www.ic.unicamp.br/~santanch/teaching/alg/2012-1/exercicios.html](
  https://www.ic.unicamp.br/~santanch/teaching/alg/2012-1/exercicios.html);

* [https://www.inf.pucrs.br/~pinho/LaproI/Exercicios/SeqDecisao/lista1.htm](
  https://www.inf.pucrs.br/~pinho/LaproI/Exercicios/SeqDecisao/lista1.htm).

* [https://dcc.ufrj.br/~leandro/mat/xbt236/Lista1.pdf](
  https://dcc.ufrj.br/~leandro/mat/xbt236/Lista1.pdf);
