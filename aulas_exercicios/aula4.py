def main():
    print(find_([1, 2, 3, 4], 3))
    print(find([1, 2, 3, 4], 3))


def find_(list_, element):
    n = len(list_)
    for i in range(n):
        if list_[i] == element:
            return i
    return None


def find(list_, element):
    for i, e in enumerate(list_):
        if e == element:
            return i


def find1(list_, element):
    """Duas buscas -> ineficiencia"""
    if element in list_:
        return list_.index(element)


if __name__ == '__main__':
    main()
