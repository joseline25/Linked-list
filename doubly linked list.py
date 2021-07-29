class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None



class DoubleLinkedList():
    def __init__(self, name):
        self.root = Node(0)
        print(" the doubly linked list named", name, "has been initialized!")


doubleList = DoubleLinkedList('test')

node1 = Node(5)
doubleList.root.next = node1
node1.previous = doubleList.root

node2 = Node(7)
node2.previous = node1
node1.next = node2

print(doubleList.root.next.next.value)
print('********')
print(doubleList.root.value)
print(doubleList.root.next.value)
print(doubleList.root.next.next.value)

print('********')
print(doubleList.root.next.next.value)
print(doubleList.root.next.next.previous.value)
print(doubleList.root.next.next.previous.previous.value)



