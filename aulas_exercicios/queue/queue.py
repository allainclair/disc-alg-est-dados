# TODO Exercicio: usar listas ligadas para implementar fila com o melhor metodo
# de insercao para facilitar o metodo "dequeue()".


class Queue:
    def __init__(self):
        self.list_ = []

    def __len__(self):
        # len(queue)
        return len(self.list_)

    def enqueue(self, value):
        self.list_.append(value)

    def dequeue(self):
        return self.list_.pop(0)


class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None


def main():
    queue = Queue()
    print(queue.list_)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print(queue.list_)

    reverse(queue)

    print(queue.list_)


def reverse(queue):
    stack = Stack()

    while len(queue) > 0:  # Teste fila vazia
        aux = queue.dequeue()
        stack.push(aux)
        print('Queue:', queue.list_)
        print(aux)
        print('Stack:', stack.stack)

    while len(stack) > 0:  # Teste pilha vazia
        aux = stack.pop()
        queue.enqueue(aux)
        print('Queue:', queue.list_)
        print(aux)
        print('Stack:', stack.stack)

    return queue

if __name__ == '__main__':
    main()
