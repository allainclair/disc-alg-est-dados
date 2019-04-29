def main():
    # n = 3
    # n = 2
    # n = 0
    # exp = 2
    # exp = 3
    # n = 100
    lista = [1, 2, 3, 4]
    result = soma_rec(lista)
    print('Soma result:', result)


def fact_iterative(n):
    value = 1
    for i in range(1, n + 1):
        value = value * i  # value *= i
    return value


def fact_recursive(n):
    if n > 0:
        return n * fact_recursive(n - 1)
    else:
        return 1

def exp_it(n, exp):
    value = 1
    for _ in range(exp):
        value = value * n
    return value


def exp_rec(n, exp):
    if exp > 0:
        return n * exp_rec(n, exp - 1)
    else:
        return 1


def soma_rec(list_, i=0):
    n = len(list_)
    print('Tamanho da lista', n)
    print('i', i)
    if i < n:
        print('list_[i]', list_[i])
        print('Chamada recursiva')
        ret = list_[i] + soma_rec(list_, i + 1)
        print('retorno da recursao', ret)
        return ret
    else:
        print('Chamada nao recursiva, retorna 0')
        return 0


if __name__ == '__main__':
    main()
