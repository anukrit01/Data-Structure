# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular LinkedList class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Inserting into Circular Linkedlist:
    # Appending method
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    # Printing the list
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    # Prepending method
    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    # Removing a Node from Circular Linkedlist
    def remove_node(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next 
                        cur = cur.next

# Testing
newlist = CircularLinkedList()
newlist.append(1)
newlist.append(2)
newlist.append(3)
newlist.append(4)
newlist.prepend(0)
newlist.remove_node(0)
newlist.remove_node(1)

newlist.print_list()