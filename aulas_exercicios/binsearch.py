# 

def binsearch(elements, element):
    i, j = 0, len(elements) - 1

    while i <= j:
        mid = (j + i) // 2
        print('i:', i, 'j:', j)
        print('mid', mid)
        if element < elements[mid]:
            j = mid - 1
        elif element > elements[mid]:
            i = mid + 1
        else:  # Porque retornar apenas no else, que eh o ultimo?
            return mid
    return False


def binsearch_r(elements, element, start, end):
    if start <= end:
        mid = (start + end) // 2
        if element < elements[mid]:
            end = mid - 1
            return binsearch_r(elements, element, start, end)
        elif element > elements[mid]:
            return binsearch_r(elements, element, mid + 1, end)
        else:
            return mid
    else:
        return False


def main():
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 20, 23]
    # elements = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    element = 5
    start, end = 0, len(elements) - 1
    print('Bin search result:', binsearch_r(elements, element, start, end))

    # i, j = 0, len(elements)
    # print('Bin serach result:', binsearch_r(elements, element, i, j))


if __name__ == '__main__':
    main()
