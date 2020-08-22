# Node Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree Class
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # Height of a binary tree
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)


# Testing
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.left.left.left = Node(7)

print(tree.height(tree.root))