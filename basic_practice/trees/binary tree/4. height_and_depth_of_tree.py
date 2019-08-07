class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None

    def height(self,node):
        if node is None:
            return -1
        return max(self.height(node.left), self.height(node.right))+1

    def depth_of_node(self, root, x):

        # Base case
        if (root == None):
            return -1

        dist = -1

        if (root.val == x):
            return dist + 1
        else:
            dist = self.depth_of_node(root.left, x)
            if dist >= 0:
                return dist + 1
            else:
                dist = self.depth_of_node(root.right, x)
                if dist >= 0:
                    return dist + 1
        return dist


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
    print(tree.height(tree.root))
    print(tree.depth_of_node(tree.root, 2))