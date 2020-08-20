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

    # Spliting the Circular Linkedlist into two halves circular linked lists
    # Let first find the length
    def __len__(self):
        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    # now lets split the linkedlist
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        curr = self.head
        prev = None

        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        prev.next = self.head

        second_list = CircularLinkedList()
        while curr.next != self.head:
            second_list.append(curr.data)
            curr = curr.next
        second_list.append(curr.data)

        self.print_list()
        print('\n')
        second_list.print_list()


# Testing
newlist = CircularLinkedList()
newlist.append(1)
newlist.append(2)
newlist.append(3)
newlist.append(4)
newlist.prepend(0)
newlist.append(5)

newlist.split_list()