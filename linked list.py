
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, name):
        self.root = Node(0)
        self.head = self.root
        self.count = 1
        print(" linked list", name, "has been initialized!")


    def AddHead(self, value):
        listhead = Node(value)
        self.head.next = listhead
        self.head = listhead
        self.count +=1





list = LinkedList(name='one')
print(list.root.value)
node1 = Node(2)


list.root.next = node1
print(node1.value)
print(node1.next)

node2 = Node(5)

node1.next = node2

print(list.root.next.value)
print(node1.next.value)



liste = LinkedList('test')
print(liste.head.value)
liste.AddHead(3)
print(liste.root.next.value)
print(liste.head.value)


