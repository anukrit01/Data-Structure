# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linkedlist class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Print the list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # Insertion methods for Doubly Linkedlist
    # Append method
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head

            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    # Prepend method
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Inserting a node before/after a node
    # Adding the node after...
    def after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                new_node.prev = curr
                nxt.prev = new_node
                return
            curr = curr.next

    # Adding the node before
    def before_node(self, key, data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                new_node.prev = prev
                return
            curr = curr.next



# Testing
new_dll = DoublyLinkedList()
new_dll.append('A')
new_dll.append('B')
new_dll.append('C')
new_dll.append('D')

new_dll.after_node('B', 'E')
new_dll.before_node('B', 'E')

new_dll.print_list()