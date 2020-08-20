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

    # Delete the node
    def delete(self, node):
        curr = self.head
        
        while curr:
            if curr == node and curr == self.head:
                # case 1: deleting the only node
                if not curr.next:
                    curr = None
                    self.head = None
                    return

                # case 2: deleting head node
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
                
            elif curr == node:
                # case 3: deleting the node other than head and tail node
                if curr.next:
                    nxt = curr.next
                    pre = curr.prev
                    pre.next = nxt
                    nxt.prev = pre
                    curr.next = None
                    curr.prev = None
                    return

                # case 4: deleting the tail node
                else:
                    pre = curr.prev
                    pre.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next

    # Remove duplicate node
    def remove_duplicate(self):
        curr = self.head
        seen = dict()

        while curr:
            if curr.data not in seen:
                seen[curr.data] = 1
                curr = curr.next
            else:
                nxt = curr.next
                self.delete(curr)
                curr = nxt


# Testing
new_dll = DoublyLinkedList()
new_dll.append(1)
new_dll.append(1)
new_dll.append('B')
new_dll.append(2)
new_dll.append('B')
new_dll.append(3)
new_dll.append('D')
new_dll.append(4)

new_dll.remove_duplicate()

new_dll.print_list()