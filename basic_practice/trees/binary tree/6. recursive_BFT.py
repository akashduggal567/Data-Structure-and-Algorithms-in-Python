""" to be completed """

class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None


if __name__ == "__main__":
    tree = BT()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    """
                   1
                 /   \
                2     3
              /  \   / \
             4    5  6  7

    """
    print(tree.root.val)
    print(tree.root.left.val)
    print(tree.root.right.val)
    print(tree.root.left.left.val)
    print(tree.root.left.right.val)
    print(tree.root.right.left.val)
    print(tree.root.right.right.val)



