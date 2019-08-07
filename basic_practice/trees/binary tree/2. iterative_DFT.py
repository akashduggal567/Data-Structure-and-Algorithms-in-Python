class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None

    def inorder_traversal(self, root):
        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.val, end=" ")
                current = current.right
            else:
                break
        print()

    def preorder_traversal(self, root):
        if root is None:
            return
        stack = []
        stack.append(root)
        """
                                 1
                               /   \
                              2     3
                            /  \   / \
                           4    5  6  7

              """
        while stack:
            root = stack.pop()
            print(root.val, end=" ")
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    def postorder_traversal(self, root):
        if root is None:
            return
        stack1 = []
        stack2 = []
        stack1.append(root)

        while stack1:
            root = stack1.pop()
            stack2.append(root)
            if root.left is not None:
                stack1.append(root.left)
            if root.right is not None:
                stack1.append(root.right)

        while stack2:
            root = stack2.pop()
            print(root.val, end=" ")


if __name__ == "__main__":
    tree = BT()
    BT.root = Node(1)
    BT.root.left = Node(2)
    BT.root.right = Node(3)
    BT.root.left.left = Node(4)
    BT.root.left.right = Node(5)
    BT.root.right.left = Node(6)
    BT.root.right.right = Node(7)
    """
                       1
                     /   \
                    2     3
                  /  \   / \
                 4    5  6  7

    """
    print("inorder: ")
    BT.inorder_traversal(tree, BT.root)
    print("\npreorder: ")
    BT.preorder_traversal(tree, BT.root)
    print("\n\npostorder: ")
    BT.postorder_traversal(tree, BT.root)




