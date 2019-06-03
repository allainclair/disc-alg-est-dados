class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)

    def remove(self, value):
        pass


def inorder(root):
    if root.left is not None:
        inorder(root.left)
    print(f'{root.value}')
    if root.right is not None:
        inorder(root.right)


def preorder(root):
    print(f'{root.value}')
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)


def postorder(root):
    if root.left is not None:
        postorder(root.left)
    if root.right is not None:
        postorder(root.right)
    print(f'{root.value}')


def main():
    root = TreeNode(10)

    value = 20
    root.insert(value)

    value = 5
    root.insert(value)

    value = 6
    root.insert(value)

    value = 30
    root.insert(value)

    value = 1
    root.insert(value)

    print('INorder')
    inorder(root)

    print('PREorder')
    preorder(root)

    print('POSTorder')
    postorder(root)


if __name__ == '__main__':
    main()
