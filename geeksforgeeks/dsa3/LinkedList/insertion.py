"""
1. insert at front
2. insert after a given node
3. insert at the end

"""


class Node:
    # to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # to initialize the LinkedList
    def __init__(self):
        self.head = None

    # function to insert the node at the beginning
    def insert_front(self, data):
        new_node = Node(data)
        # if list is empty yet
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # function to insert the node at the end
    def insert_end(self, data):
        new_node = Node(data)
        ptr = self.head

        # run loop till last node pointer points to null
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node

    # function to insert after a node
    def insert_after(self, val, data):
        new_node = Node(data)
        ptr = self.head
        while ptr.data != val:
            ptr = ptr.next
        new_node.next = ptr.next                    # new_node points to the same node as ptr node
        ptr.next = new_node                         # ptr node points to the new_node

    def print_list(self):
        # pointer pointing to the node same as head
        ptr = self.head
        # run loop till ptr reaches last node
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next


if __name__ == "__main__":

    S_list = LinkedList()
    S_list.insert_front(0)
    S_list.insert_after(0, 1)
    S_list.insert_after(1, 2)
    S_list.insert_end(3)
    S_list.print_list()

