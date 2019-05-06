"""
1. Criar hash com tamanho fixo (size)
2. Nossa estrutura de dados hash eh uma lista de Nones inicialmente.
3. Para adicionar um elemento, temos que calcular um endereco para esse
   elemento. O endereco eh o resultado da multiplicacao do element com um
   numero primo e depois faz-se o "mod" (%) com o tamanho da hash.
4. Com isso temos o indice de nossa lista de onde colocaremos o elemento.
5. Isso faz com que possamos acessar esse indice diretamente sem precisar
   andar pela lista, ou fazer uma busca binaria nela. Basta saber o endereco
   com a funcao de hash, e temos acesso a esse elemento.
6. Dessa forma, ao adicionar um elemento, calcula-se o endereco dele,
   e ele eh colocado nesse endereco da lista.
7. Para busca o elemento adicionado, novamente calcula-se o endereco dele e
   verifica-se se ele esta la. Elementos que nao estao na hash vao retornar
   False.
"""

BIG_PRIME = 6_700_417


def main():
    size = 1000
    hash_ = create_hash(size)

    element = 100
    add_to_hash(hash_, element)

    element = 200
    add_to_hash(hash_, element)

    element = 541657531
    add_to_hash(hash_, element)

    print()
    print(search_element(hash_, 50))
    print(search_element(hash_, 100))
    print(search_element(hash_, 200))
    print(search_element(hash_, 1))
    print(search_element(hash_, 54))
    print(search_element(hash_, 541657531))


def calc_address(element, size):
    # "Hash function".
    # Usar a funcao hash do python para usar outros elementos nao numericos.
    address = BIG_PRIME * element % size
    print('address', address)
    return BIG_PRIME * element % size


def create_hash(size=1000):
    return [None]*size


def add_to_hash(hash_, element):
    address = calc_address(element, len(hash_))
    hash_[address] = element


def search_element(hash_, element):
    address = calc_address(element, len(hash_))
    if hash_[address] is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
