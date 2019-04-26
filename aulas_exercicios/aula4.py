def main():
    # element = 3
    # element = 'x'
    element = 10
    # element = 1.0
    # element = 'joao'
    list_ = [1, 0, 2, 1, 2, 1, 1]  # 8
    print(recursive_sum(list_))
    # return_ = find1(list_, element)
    # print('Find encontrou na posicao?', return_)
    # print(find([1, 2, 3, 4], 3))


def find_(list_, element):
    """Find que cria uma lista com os respectivos indicies do "element"."""
    n = len(list_)
    return_list = []
    for i in range(n):
        print('Indice i', i)
        print('element', element)
        print('list_[i]', list_[i])
        if list_[i] == element:
            print('element == list_[i]')
            return_list.append(i)
        else:
            print('element != list_[i]')
    return return_list


def find(list_, element):
    for i, e in enumerate(list_):
        print('i', i)
        print('e', e)
        print('element', element)
        if e == element:
            return i


def find1(list_, element):
    """Duas buscas -> ineficiencia"""
    if element in list_:
        return list_.index(element)


def recursive_sum(list_, i=0):
    n = len(list_)
    print('Tamanho da lista', n)
    print('i', i)
    if i < n:
        print('list_[i]', list_[i])
        print('Chamada recursiva...')
        ret = list_[i] + recursive_sum(list_, i + 1)
        print('Retorno da recursao i =', i, 'retorno:', ret)
        return ret
    else:
        print('Chamada nao recursiva, retorna 0')
        return 0


if __name__ == '__main__':
    main()
