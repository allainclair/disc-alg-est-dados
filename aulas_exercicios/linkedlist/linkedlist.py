class List:
    def __init__(self):
        # "Variavel global" dentro no escopo/contexto da classe."
        self.first_node = None

    def __str__(self):
        """Metodo especial que eh chamado quando o print() eh usado no objeto."""
        node = self.first_node
        string = ''
        while node is not None:
            string += f'{node.value}, '  # string = string + f'{node.value} '
            node = node.next
        return string

    def __len__(self):
        """Implementar o tamanho a lista."""
        node = self.first_node
        size = 0
        while node is not None:
            size += 1
            node = node.next
        return size

    def add_sorted(self, value):
        """Usar essa adicao desde o inicio para manter lista ligada."""
        new_node = Node(value)  # Cria-se novo node.

        if not self.empty():  # Se a lista nao eh vazia.
            # Var auxiliar para nao perder referencia do primeiro node.
            node = self.first_node
            # Se o "campo next" nao eh None continuamos andando na lista para
            # chegar ao ultimo node.
            print('node.value', node.value)
            print('value', value)
            endlist = False
            startlist = False
            i = 0
            while node.value <= value and not startlist and node.next is not None:
                node = node.next
                if node.value <= value and i == 0:
                    new_node.next = node
                    # new_node.next = node.next
                    # node.next = new_node
                    # endlist = True
                    startlist = True
                i += 1
            print(value)
            print()
            # Quando o "node" auxiliar esta com "node.next == None"
            # atribuimos a "node.next" o novo node.
            # if startlist:
            #     new_node.next = node
            # else:
            new_node.next = node.next
            node.next = new_node
        else:  # Se a lista esta vazia, o novo node eh o primeiro node.
            self.first_node = new_node

    def addat_end(self, value):
        """Adiciona ao final da lista ligada.

        TODO Exercicio: Adicionar apenas elementos nao repetidos
        """
        new_node = Node(value)  # Cria-se novo node.
        # if self.first_node is not None:  # Se a lista nao eh vazia.
        if not self.empty():  # Se a lista nao eh vazia.
            # Var auxiliar para nao perder referencia do primeiro node.
            node = self.first_node
            # Se o "campo next" nao eh None continuamos andando na lista para
            # chegar ao ultimo node.
            while node.next is not None:
                node = node.next
            # Quando o "node" auxiliar esta com "node.next == None"
            # atribuimos a "node.next" o novo node.
            node.next = new_node
            # new_node.next = None
        else:  # Se a lista esta vazia, o novo node eh o primeiro node.
            self.first_node = new_node

    def addat_start(self, value):
        """Adiciona "value" ao comeco da lista ligada."""
        new_node = Node(value)
        new_node.next = self.first_node  # Novo node ja aponta para o primeiro.
        self.first_node = new_node  # Primeiro node se torna o novo node.

    def empty(self):
        return self.first_node is None  # self.first_node == None

    def remove(self, value):
        """Return true if the value was found and removed; otherwise False."""
        node = self.first_node
        while node.next is not None:
            if node.next.value == value:
                print('node.next.value', node.next.value)
                node.next = node.next.next
                print('node.next.next.value', node.next.next.value)
                # del node.next
                return True
            node = node.next
        return False

    def reset(self):
        """Reset the list to size 0"""
        node = self.first_node
        while node.next is not None:
            node_to_del = node
            node = node.next
            del node_to_del
        self.first_node = None

    def print_(self):
        aux_node = self.first_node
        # while aux_node != None:
        while aux_node is not None:
            print(aux_node.value, end=', '),
            aux_node = aux_node.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def main():
    addat_start_tests()
    # addat_end_tests()
    # add_sorted_tests()


def add_sorted_tests():
    print('Add sorted tests')
    list_ = List()  # Nova lista.
    list_.add_sorted(1)
    list_.add_sorted(2)
    list_.add_sorted(3)
    list_.add_sorted(0)
    list_.add_sorted(6)
    list_.add_sorted(7)
    list_.add_sorted(10)
    list_.add_sorted(8)
    list_.add_sorted(5)
    list_.add_sorted(1)
    # list_.print_()
    print(list_)
    print()


def addat_end_tests():
    print('Addat end tests')
    list_ = List()  # Nova lista.
    list_.addat_end(1)
    list_.addat_end(2)
    list_.addat_end(3)
    list_.addat_end(4)
    list_.addat_end(5)
    # list_.print_()
    print(list_)
    print(len(list_))
    print()


def addat_start_tests():
    print('Addat start tests')
    list_ = List()  # Nova lista.
    # list_.addat_start(2)
    # list_.addat_start(3)
    # list_.addat_start(5)
    # list_.addat_start(1)
    for i in range(5):
        list_.addat_start(i)
    # list_.print_()
    print(list_)
    # list_.len_()
    print('len(list_)', len(list_))
    print()
    list_.remove(2)
    # print(list_)
    list_.print_()



if __name__ == '__main__':
    main()
