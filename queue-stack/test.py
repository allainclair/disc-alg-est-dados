import random


def push(stack, element):
    stack.append(element)


def pop(stack, element=None):
    return stack.pop() if stack else False


def dequeue(queue, element=None):
    return queue.pop(0) if queue else False


def enqueue(queue, element):
    queue.append(element)


def ex1(rules):
    return_ = []
    elements = random.sample(range(0, 100), 12)
    for element in elements:
        index = element % 4
        list_, func = rules[index]
        ret = func(list_, element)
        if index == 1 or index == 3:
            return_.append(ret)
    stack, func = rules[0]
    queue, func = rules[2]
    print('in:', elements)
    print('out', return_)
    print('stack', stack)
    print('queue', queue)


def ex2(rules):
    return_ = []
    elements = random.sample(range(0, 100), 12)
    for element in elements:
        index = element % 4
        list_, func = rules[index]
        ret = func(list_, element)
        if index == 1 or index == 3:
            return_.append(ret)
    stack, func = rules[2]
    queue, func = rules[0]
    print('in:', elements)
    print('out', return_)
    print('stack', stack)
    print('queue', queue)


def main():
    stack = []
    queue = []
    rules1 = [(stack, push), (stack, pop), (queue, enqueue), (queue, dequeue)]
    rules2 = [(queue, enqueue), (queue, dequeue), (stack, push), (stack, pop)]

    # ex1(rules1)
    ex2(rules2)


if __name__ == '__main__':
    main()
