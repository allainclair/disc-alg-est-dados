class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        print('node.value', node.value)
        print('node.next', node.next)

    def add(self, value):
        self.next = Node(value)
        # self = self.next

#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#
#     node1.next = node2
#     node2.next = node3
#
#     node.print()


def imprimir_lista(lista):
    node = lista
    while node != None:
        print('lista.value', node.value)
        node = node.next


def adicionar_ordenado(lista, valor):
    if lista is not None:
        prox = lista
        ant = None
        while prox.value <= valor:
            ant = prox
            prox = prox.next

        novo = Node(valor)
        if ant is not None:
            ant.next = novo
            novo.next = prox
        else:
            novo.next = prox
            lista = novo





def adicionar_no_fim(lista, valor):
    if lista is not None:
        node = lista
        while node.next != None:
            node = node.next
        # node.next == None
        node.next = Node(valor)
    else:
        lista = Node(valor)
        print('Primeiro elemento adicionado', lista.value)
        return lista


def criar_lista(value):
    return Node(value)


if __name__ == '__main__':
    lista = criar_lista(100)
    imprimir_lista(lista)

    adicionar_ordenado(lista, 10)
    # print()
    imprimir_lista(lista)
    # adicionar_no_fim(lista, 11)
    # print()
    # imprimir_lista(lista)


    # print('lista.value', lista.value)
    # node = lista.next
    # print('lista.value', lista.value)
