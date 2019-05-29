# TODO Exercicio: usar listas ligadas para implementar pilha com o melhor metodo
# de insercao para facilitar o metodo "pop()".
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
    # stack1 = Stack()
    # stack2 = Stack()
    #
    # n = 10
    # for i in range(n):
    #     stack1.push(i)
    #
    # print(stack1.stack)
    #
    # for _ in range(n):
    #     print(stack1.pop())
    #
    # print(stack1.pop())
    list_ = [10, 10, '+', 20, '+', 2, 2, '*', '*', 1.1, '*']
    result = calc_sufix(list_)
    print('Resultado do calc_sufix:', result)


def calc_sufix(list_):
    stack = Stack()
    for element in list_:
        str_element = str(element)
        # Se for numero.
        if isinstance(element, int) or isinstance(element, float):
            stack.push(str_element)
        else:  # Se for operador.
            operand2, operand1 = stack.pop(), stack.pop()
            aux_value = eval(operand1 + str_element + operand2)
            stack.push(str(aux_value))
        print(stack.stack)
    print('Tamanho da pilha:', len(stack))
    return stack.pop()


if __name__ == '__main__':
    main()
