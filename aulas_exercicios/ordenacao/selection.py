def selection_sort(list_):
    len_ = len(list_)
    for i in range(len_ - 1):  # -1?
        min_ = i
        for j in range(i+1, len_):
            if list_[j] < list_[min_]:
                min_ = j
        # Troca de elementos.
        list_[i], list_[min_] = list_[min_], list_[i]
        # list_[i] agora contem seu elemento na ordem correta.
    return list_


def partition(list_, low, high):
    """Funcao que particiona a lista tal que temos um pivo separador:
    todos elementos a esquerda do pivo sao menores que ele; todos a direita sao
    maiores ele. O pivo eh colocado na posicao correta do intervalo low, high.
    Tambem retorna o novo indice do pivo.
    """
    print(list_)
    pivot = list_[high]
    print('pivot', pivot)
    # Indice do menor elemento que sera ao final o indice do pivo.
    min_ = low - 1

    for i in range(low, high):  # Percorre de low ateh high - 1!
        if list_[i] <= pivot:
            min_ += 1
            print('min_', min_)
            print('i', i)
            print('list_[min_]', list_[min_])
            print('list_[i]', list_[i])
            list_[min_], list_[i] = list_[i], list_[min_]
            print(list_)
            print()

    # Coloca pivo na posicao correta, elemento que esta ocupando a posicao
    # do pivo vai para o final (que era a posicao incial do pivo).
    print('list_[min_ + 1]', list_[min_ + 1])
    print('list_[high]', list_[high])
    list_[min_ + 1], list_[high] = list_[high], list_[min_ + 1]
    print('Pivot position', min_ +1)
    print(list_)

    # Retorna a posicao do pivo, que eh a posicao de ordenacao que ele deve estar
    # nesse intervalo [low, high].
    return min_ + 1


def quick_sort(list_, low, high):
    if low < high:
        partition_index = partition(list_, low, high)
        quick_sort(list_, low, partition_index - 1)
        quick_sort(list_, partition_index + 1, high)
    return list_


def main():
    l = [1, 3, 7, 10, 9, 12, 4]
    # print(l)
    # l = selection_sort(l)
    # print(l)

    # print(quick_sort(l, 0, len(l) - 1))
    partition(l, 0, len(l)- 1)


if __name__ == '__main__':
    main()
