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