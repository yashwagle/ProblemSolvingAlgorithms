
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def setNext(self, nextitem):
        self.next = nextitem

    def setData(self, item):
        self.data = item

    def getNext(self):
        return self.next


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        n = Node(item)
        if self.head == None:
            self.head = n
        else:
            n.setNext(self.head)
            self.head = n

    def append(self, item):
        n = Node(item)
        pos = self.head
        prev = None
        while pos!=None:
            prev = pos
            pos = pos.getNext()
        if prev == None:
            self.head = n
        else:
            prev.setNext(n)

    def insert(self, item, position):
        n = Node(item)
        if position==0:
            n.setNext(self.head)
            self.head = n
            return
        i = 0
        pos = self.head
        prev = None
        while i < position:
            i = i + 1
            prev = pos
            pos = pos.getNext()
        n.setNext(pos)
        prev.setNext(n)

    def display(self):
        n = self.head
        print('The list is')
        while n != None:
            print(n.getData(),end=' ')
            n = n.getNext()
        print()


    def search(self, item):
        n = self.head
        found = False
        while n!= None and found == False:
            if n.getData() == item:
                found = True
            else:
                n = n.getNext()
        return found

    def size(self):
        s = 0
        n = self.head
        while n != None:
            s = s + 1
            n = n.getNext()
        return s

    def remove(self, item):
        point =self.head
        previous = None
        found = False
        while not found:
            if point.getData() == item:
                found = True
            else:
                previous = point
                point = point.getNext()

        if previous == None:
            self.head = self.head.getNext()
        else:
            previous.setNext(point.getNext())

    def slice(self, startpos, endpos):
        i = 0
        start = self.head
        slicedList = UnorderedList()
        while i< startpos:
            start = start.getNext()
            i = i+1
        while i<endpos:
            slicedList.append(start.getData())
            i = i + 1
            start = start.getNext()
        return slicedList



def driver():
    un = UnorderedList()
    un.add(1)
    un.add(2)
    un.add(3)
    un.add('hey')
    un.display()
    print(un.search(5))
    print(un.size())
    un.remove('hey')
    un.add(6)
    un.add('dog')
    un.add('cat')
    un.add('rat')
    sliced = un.slice(3,6)
    sliced.display()
    un.display()

driver()

