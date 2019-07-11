
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
        self.prev = None

    def setData(self,item):
        self.data = item

    def getData(self):
        return self.data

    def setNext(self, add):
        self.next = add

    def getNext(self):
        return self.next

    def setPrev(self, add):
        self.prev = add

    def getPrev(self):
        return self.prev

class DoublyEndedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def add(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n

    def display(self):
        curr = self.head
        print('The list is')
        while curr!=None:
            print(curr.getData(),end=' ')
        print()

    def insert(self, item, pos):
        i = 0
        n = Node(item)
        curr = self.head
        while i<pos:
            curr = curr.getNext()
            i = i + 1
        n.setNext(curr)
        n.setPrev(curr.getPrev())
        ch = curr.getPrev()
        ch.setNext(prev)
        curr.setPrev(n)

    def append(self, item):
        n = Node(item)
        n.setPrev(self.end)
        self.end = n

    def search(self, item):
        curr = self.head
        while curr!= None:
            if curr.getData() == item:
                return True
            curr = curr.getNext()
        return False

    def remove(self, item):
        curr = self.head
        while curr!=None and curr.getData() != item:
            curr = curr.getNext()
        if curr == None:
            return False
        if curr == self.head:
            self.head = curr.getNext()
            self.head.setPrev(None)
            return True
        prev = curr.getPrev()
        prev.setNext(curr.getNext())
        curr = curr.getNext()
        curr.setPrev(prev)
        return False
