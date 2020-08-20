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

    # Removing a Node from Circular Linkedlist
    def remove_node(self, node):
        if self.head:
            if self.head == node:
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
                    if cur == node:
                        prev.next = cur.next 
                        cur = cur.next

    '''
    Josephus Problem: Given a step count, after traversing that much steps on the circular linkedlist
    the node will be removed on which the current control is present.
    '''
    def josephus_circle(self, step):
        curr = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            print('KILL:' + str(curr.data))
            self.remove_node(curr)
            curr = curr.next


# Testing
newlist = CircularLinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.append('D')
newlist.append('E')

newlist.josephus_circle(2)
print('\nRemainig Node:')
newlist.print_list()