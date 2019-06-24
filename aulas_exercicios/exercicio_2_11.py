BASE = 10


def inverso(n):
    inverso_ = n % BASE
    quociente = n // BASE
    while quociente > 0:
        resto = quociente % BASE
        quociente //= BASE
        inverso_ *= BASE
        inverso_ += resto
    return inverso_


def main():
    print('Resultado', inverso(123))
    print('Resultado', inverso(732))
    print('Resultado', inverso(987654321))


if __name__ == '__main__':
    main()
