class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None

    def level_order(self,root):
        if root is None:
            return

        queue = []
        queue.append(root)

        while len(queue)> 0:
            print(queue[0].val, end=" ")

            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

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
    tree.level_order(tree.root)
