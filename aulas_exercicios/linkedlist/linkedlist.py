class Node:
    def __init__(self, value):
        self.value = value
        self.next_ = None

    def add(self, value):
        self.next_ = Node(value)
        self = self.next_
