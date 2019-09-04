import random
import collections  # NAO USE ESSE MODULO, EH APENAS PARA EXEMPLO

NUM_ELEMENTS = 1000

class Stack:
    def __init__(self):
        self.list_ = []

    def push(self, value):
        self.list_.append(value)

    def pop(self):
        return self.list_.pop()


class Deque:
    def __init__(self):
        self.pilha = Stack()
        self.aux = Stack()

    def append(self, element):
        self.pilha.push(element)

    def appendleft(self, element):
        while len(self.pilha.list_) != 0:
            self.aux.push(self.pilha.pop())
        self.aux.push(element)
        while len(self.aux.list_) != 0:
            self.pilha.push(self.aux.pop())

    def pop(self):
        if len(self.pilha.list_) == 0:
            return False
        else:
            return self.pilha.pop()

    def popleft(self):
        if len(self.pilha.list_) == 0:
            return False
        else:
            while len(self.pilha.list_) > 0:
                self.aux.push(self.pilha.pop())
            saida = self.aux.pop()
            while len(self.aux.list_) > 0:
                self.pilha.push(self.aux.pop())

def test_simple():
    dq = Deque()  # Fila que tem "duas pontas"

    assert dq.append(10) is None  # Append 10 e nao retorna nada.
    assert dq.append(20) is None  # Append 20 e nao retorna nada.
    assert dq.append(30) is None  # ...
    assert dq.append(40) is None

    assert dq.pop() == 40  # Pop retorna 40 (pop tira da direita)
    assert dq.pop() == 30  # ...
    assert dq.pop() == 20
    assert dq.pop() == 10

    assert dq.pop() is False  # Deque vazia.
    assert dq.pop() is False  # ...

    assert dq.appendleft(40) is None
    assert dq.appendleft(50) is None

    assert dq.popleft() == 50

    assert dq.append(100) is None
    assert dq.append(200) is None

    assert dq.popleft() == 40
    assert dq.pop() == 200

    assert dq.appendleft(300) is None

    assert dq.pop() == 100
    assert dq.pop() == 300
    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def test_random():
    dq = Deque()

    append, appendleft, = [], []
    for _ in range(NUM_ELEMENTS):
        element = random.randint(-1000, 1000)
        if random.random() > 0.5:  # Probabilidade de 50%
            dq.append(element)
            append.append(element)
        else:
            dq.appendleft(element)
            appendleft.append(element)

    for element in reversed(append):
        assert dq.pop() == element

    for element in reversed(appendleft):
        assert dq.popleft() == element

    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def main():
    test_simple()
    test_random()


if __name__ == '__main__':
    main()
