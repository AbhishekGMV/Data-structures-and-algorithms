def inorderTraversal(node):
    if not node:
        return 
    inorderTraversal(node.left)
    print(node.value)
    inorderTraversal(node.right)

def preOrderTraversal(node):
    if not node:
        return 
    print(node.value)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def postOrderTraversal(node):
    if not node:
        return 
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.value)

class Node:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.right = n2
n1.left = n3
n2.left = n4

inorderTraversal(n1)
print("-----")
preOrderTraversal(n1)
print("-----")
postOrderTraversal(n1)
