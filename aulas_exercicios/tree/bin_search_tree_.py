class BinSerachTreeNode:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left != None:
                self.left.insert(new_value)
            else:
                self.left = BinSerachTreeNode(new_value)
        else:
            if self.right != None:
                self.right.insert(new_value)
            else:
                self.right = BinSerachTreeNode(new_value)

    # def inorder(self, node):
    #     if node.left is not None:
    #         self.inorder(node.left)
    #     print(self.value)
    #     if node.right is not None:
    #         self.inorder(node.right)


def inorder(tree_node):
    if tree_node.left is not None:
        inorder(tree_node.left)
    print(tree_node.value)  # Processar o tree_node
    if tree_node.right is not None:
        inorder(tree_node.right)


def preorder(tree_node):
    print(tree_node.value)  # Processar o tree_node
    if tree_node.left is not None:
        preorder(tree_node.left)
    if tree_node.right is not None:
        preorder(tree_node.right)


def postorder(tree_node):
    if tree_node.left is not None:
        postorder(tree_node.left)
    if tree_node.right is not None:
        postorder(tree_node.right)
    print(tree_node.value)  # Processar o tree_node


def main():
    value = 10
    root = BinSerachTreeNode(value)

    value = 15
    root.insert(value)

    value = 20
    root.insert(value)

    value = 2
    root.insert(value)

    value = 3
    root.insert(value)

    value = 0
    root.insert(value)

    value = 7
    root.insert(value)

    print('INorder')
    inorder(root)
    print('PREorder')
    preorder(root)
    print('POSTorder')
    postorder(root)

    print('INorder class')
    root.inorder(root)


if __name__ == '__main__':
    main()
