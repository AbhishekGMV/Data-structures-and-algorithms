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
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextNode = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = nextNode
        self.head = prev

        return prev


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
ll = LinkedList(n1)

ll.reverse()
ll.traverse()