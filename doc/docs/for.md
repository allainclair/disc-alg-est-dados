```Python
# For simples.

elementos = ['a', 'b', 'c', 'd']

for elemento in elementos:
    print(elemento)

a
b
c
d
```

```Python
# For com a funcao range().

for i in range(5):
    print(i)

0
1
2
3
4
```

```Python
# For aninhado.

n = m = 3
for i in range(n):
    for j in range(m):
        print('i, j: ', i, ', ', j, sep='')
        # print(f'i, j: {i}, {j}')

i, j: 0, 0
i, j: 0, 1
i, j: 0, 2
i, j: 1, 0
i, j: 1, 1
i, j: 1, 2
i, j: 2, 0
i, j: 2, 1
i, j: 2, 2
```

```Python
# For com "IF".

n, m = 4, 6  # n = 4 e m = 6
for i in range(n):
    for j in range(m):
        if i == j:
            print('i, j: ', i, ', ', j, sep='')
            # print(f'i, j: {i}, {j}')


i, j: 0, 0
i, j: 1, 1
i, j: 2, 2
```

```Python
# Elementos "enumerados" usando a funcao "enumerate()".
# Similar a usar "range()".

elementos = ['a', 'b', 'c', 'd']
for i, elemento in enumerate(elementos):
    print(f'Elemento {i}: {elemento}')

Elemento 0: a
Elemento 1: b
Elemento 2: c
Elemento 3: d

# Elementos iniciando em 1.
for i, elemento in enumerate(elementos, 1):
    print(f'Elemento {i}: {elemento}')

Elemento 1: a
Elemento 2: b
Elemento 3: c
Elemento 4: d
```