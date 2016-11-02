"""
    Author: Afroze Khan
    Created: 11/2/2016
    Description: Program to implement single linked list
"""

class Node(object):
    nxt = None
    def __init__(self, value):
        self.value = value

class SingleLinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.nxt != None:
            current = current.nxt
        current.nxt = node

    def delete(self, value):
        if self.head:
            current = self.head
            if current.value == value:
                self.head = self.head.nxt
                return
            while current.nxt and current.nxt.value != value:
                current = current.nxt
            current.nxt = current.nxt.nxt

    def display(self):
        current = self.head
        while current.nxt:
            print current.value, "->"
            current = current.nxt
        print current.value

    def sort(self):
        pass
objLinkList = SingleLinkedList()
values = [1, 4, 2, 10, 6,5,3]
for val in values:
    node = Node(val)
    objLinkList.insert(node)
print "After inserting values:"
objLinkList.display()
print "Deleting 1"
objLinkList.delete(1)
objLinkList.display()
print "Deleting 10"
objLinkList.delete(10)
objLinkList.display()
print "Deleting 3"
objLinkList.delete(3)
objLinkList.display()

"""
Output:
After inserting values:
1 ->
4 ->
2 ->
10 ->
6 ->
5 ->
3
Deleting 1
4 ->
2 ->
10 ->
6 ->
5 ->
3
Deleting 10
4 ->
2 ->
6 ->
5 ->
3
Deleting 3
4 ->
2 ->
6 ->
5
"""