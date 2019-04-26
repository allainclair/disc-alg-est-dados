# arquivo binsearch.py

def soma(list_, i):
    n = len(list_)
    print('Tamanho da lista', n)
    print('i', i)
    if i < n:
        print('list_[i]', list_[i])
        print('Chamada recursiva')
        ret = list_[i] + soma(list_, i + 1)
        print('retorno da recursao', ret)
        return ret
    else:
        print('Chamada nao recursiva, retorna 0')
        return 0


def recursive_exp(n, exp, i=0):
    print('i', i)
    if i < exp:
        print('Chamada recursiva...')
        ret = recursive_exp(n, exp, i + 1)
        print('Retorno da recursao i =', i, 'retorno:', ret)
        return n * ret
    else:
        print('Retorno nao recursivo, retorna 1')
        return 1
