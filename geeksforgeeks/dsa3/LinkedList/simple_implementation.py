class Node:
    # to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # to initialize the LinkedList
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    S_list = LinkedList()
    # initialize 3 node objects
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    # linking the nodes with each other
    S_list.head = first_node
    S_list.head.next = second_node
    second_node.next = third_node

    # printing nodes
    print(S_list.head.data)
    print(S_list.head.next.data)
    print(S_list.head.next.next.data)
