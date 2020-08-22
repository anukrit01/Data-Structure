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


    # Depth-First Traversal
    # Pre-order Traversal
    def preorder(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal 


    # In-order Traversal
    def inorder(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right, traversal)
        return traversal


    # Post-order Traversal
    def postorder(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal 



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

print(tree.preorder(tree.root, ''))
print(tree.inorder(tree.root, ''))
print(tree.postorder(tree.root, ''))