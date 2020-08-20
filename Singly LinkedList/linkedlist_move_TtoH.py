# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion as append
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Print the list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    # Insertion using prepend
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    # Insertion after a given node
    def after_node(self, pre_node, data):
        if not pre_node:
            print('Previous node does not exist.')
            return
        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    # Moving the tail to head position in linkedlist
    def move_tail_to_head(self):
        if self.head and self.head.next:
            p = self.head
            prev = None

            while p.next:
                prev = p
                p = p.next
            p.next = self.head
            prev.next = None
            self.head = p


# Testing
newlist = LinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.prepend('D')
newlist.after_node(newlist.head.next, 'E')

newlist.print_list()

newlist.move_tail_to_head()
newlist.print_list()