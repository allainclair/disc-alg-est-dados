def main():
    list_ = [1, 2, 3, 'joao', 'maria']
    element = [1, 2, 3]

    return_ = my_in(element, list_)
    print(return_)


def my_in(element, list_):
    for e in list_:
        if e == element:
            return True
    #    else:
    #        return False
    return False


def remove(lista, elemento):
    lista.remove(elemento)


if __name__ == '__main__':
    main()
