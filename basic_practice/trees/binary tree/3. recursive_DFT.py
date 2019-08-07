class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None

    def recur_inorder(self, root):
        if root:
            self.recur_inorder(root.left)
            print(root.val, end=" ")
            self.recur_inorder(root.right)

    def recur_postorder(self, root):
        if root:
            self.recur_postorder(root.left)
            self.recur_postorder(root.right)
            print(root.val, end=" ")

    def recur_preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.recur_preorder(root.left)
            self.recur_preorder(root.right)


if __name__ == "__main__":
    tree = BT()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    """
                   1
                 /   \
                2     3

    """
    print("Inorder")
    tree.recur_inorder(tree.root)
    print("\nPostorder")
    tree.recur_postorder(tree.root)
    print("\nPreorder")
    tree.recur_preorder(tree.root)


