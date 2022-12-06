class Node:
    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, head):
        self.head = head

    def bfs(self):
        root = self.head
        q = [root]

        while q:

            node = q.pop()
            print(node.value)

            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

    def recursiveBfs(self, q):
        if not q:
            return

        node = q.pop()
        print(node.value)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

        self.recursiveBfs(q)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.right = n2
n1.left = n3
n2.left = n4

tree = BinaryTree(n1)
tree.bfs()
print()
tree.recursiveBfs([n1])
