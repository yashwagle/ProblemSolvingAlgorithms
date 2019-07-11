
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
        self.length = 0

    def add(self, item):
        n = Node(item)
        self.length = self.length + 1
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
        self.length = self.length + 1

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
        self.length = self.length + 1

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
        while not found and point!=None:
            if point.getData() == item:
                found = True
            else:
                previous = point
                point = point.getNext()
        if found == False:
            return False
        if previous == None:
            self.head = self.head.getNext()
        else:
            previous.setNext(point.getNext())
        self.length = self.length - 1
        return True

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
    print(sliced.remove('rat'))
    sliced.display()
    un.display()

#driver()

def ULinput():
    ch = 0
    un = UnorderedList()
    while ch!=8:
        ch=input('Enter choice 1: Add 2: Insert 3:Append 4:Remove 5:Display 6:length 7:slice 8:exit')
        if ch == '1':
            item = input('Enter the item')
            un.add(item)
        elif ch == '2':
            item = input('Enter the item')
            pos = input('Enter the position')
            un.insert(item,int(pos))
        elif ch=='3':
            item = input('Enter the item')
            un.append(item)
        elif ch=='4':
            item = input('Enter item to be removed')
            if un.remove(item):
                print('Delete successsful')
            else:
                print('Item not found Delete failed')
        elif ch=='5':
            un.display()
        elif ch=='6':
            print(un.length)
        elif ch=='7'1:
            start = input('enter start position')
            end = input('enter end position')
            sliced = un.slice(int(start), int(end))
            print('Slice list is')
            sliced.display()


ULinput()

