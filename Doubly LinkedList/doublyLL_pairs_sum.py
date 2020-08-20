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


    # Number of Pairs with sum equal to given value
    def pair_sum(self, sum_value):
        p = self.head
        q = None
        pairs = list()

        while p:
            q = p.next
            while q:
                if (p.data + q.data) == sum_value:
                    pairs.append('(' + str(p.data) + ',' + str(q.data) + ')')
                q = q.next
            p = p.next
        return pairs


# Testing
new_dll = DoublyLinkedList()
new_dll.append(1)
new_dll.append(2)
new_dll.append(3)
new_dll.append(4)
new_dll.append(5)

print(new_dll.pair_sum(6))