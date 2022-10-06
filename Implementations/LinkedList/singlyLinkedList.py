class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head):
        self.head = head

    def traverse(self):
        head = self.head

        while head:
            print(head.value)
            head = head.nextNode

    def insertAtStart(self, node):
        if not self.head:
            self.head = node
            return
        head = self.head
        node.nextNode = head
        self.head = node

    def insertAtEnd(self, node):
        if not self.head:
            self.head = node
            return
        head = self.head
        while head.nextNode:
            head = head.nextNode
        head.nextNode = node

    def deleteFromStart(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.nextNode
        temp = None

    def deleteFromEnd(self):
        if not self.head:
            return 
        head = self.head
        while head.nextNode.nextNode:
            head = head.nextNode
        head.nextNode = None

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
ll = LinkedList(n1)
ll.traverse()
ll.deleteFromStart()
ll.deleteFromEnd()
ll.traverse()
