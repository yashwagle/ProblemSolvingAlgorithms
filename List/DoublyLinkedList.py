
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
        curr = self.head
        if curr == None:
            self.head = n
            self.end= n
            return
        n.setNext(curr)
        curr.setPrev(n)
        self.head = n
        if self.end == None:
            self.end = n

    def display(self):
        curr = self.head
        print('The list is')
        while curr!=None:
            print(curr.getData(),end=' ')
            curr = curr.getNext()
        print()

    def insert(self, item, pos):
        i = 0
        n = Node(item)
        curr = self.head
        if pos == 0:
            self.add(item)
            return
        while i<pos:
            curr = curr.getNext()
            i = i + 1
        n.setNext(curr)
        n.setPrev(curr.getPrev())
        ch = curr.getPrev()
        ch.setNext(n)
        curr.setPrev(n)

    def append(self, item):
        n = Node(item)
        if self.head==None:
            self.head =n
            self.end = n
            return
        last = self.end
        last.setNext(n)
        n.setPrev(last)
        self.end = n
        if self.head == None:
            self.head = n

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
        if curr == None and curr.getData()!=item:
            return False
        if curr == self.head:
            self.head = curr.getNext()
            self.head.setPrev(None)
            return True
        prev = curr.getPrev()
        prev.setNext(curr.getNext())
        if curr == self.end:
            self.end = prev
        curr = curr.getNext()
        if curr!=None:
            curr.setPrev(prev)
        return True


    def reverse(self):
        curr = self.end
        while curr!= None:
            print(curr.getData(),end=' ')
            curr = curr.getPrev()
        return

    def slice(self, startpos, endpos):
        sliced = DoublyEndedList()
        curr = self.head
        i = 0
        while i < startpos:
            curr = curr.getNext()
            i = i + 1
        while i < endpos:
            sliced.append(curr.getData())
            curr = curr.getNext()
            i = i + 1
        return sliced


def driver():
    ch = 0
    dl =DoublyEndedList()
    while ch!=8:
        ch = input('Enter choice 1:Add 2: Insert 3:Append 4:Remove 5:Display 6:slice 7:Search 8:reverse')
        if ch=='1':
            item = input('Enter item')
            dl.add(item)
        elif ch=='2':
            item = input('Enter item to be inserted')
            pos = input('Enter position')
            dl.insert(item,int(pos))
        elif ch == '3':
            item = input('Enter item to be appended')
            dl.append(item)
        elif ch == '4':
            item = input('Enter item to be removed')
            if dl.remove(item):
                print('Delete successful')
            else:
                print('Delete failed!!! Item not found')
        elif ch=='5':
            dl.display()
        elif ch=='6':
            start = input('Enter start position')
            end = input('Enter the end position')
            sliced = dl.slice(int(start),int(end))
            print('Sliced list is')
            sliced.display()
        elif ch=='7':
            item = input('Enter item to be searched')
            if dl.search(item):
                print('item found')
            else:
                print('item not found')
        elif ch=='8':
            dl.reverse()


driver()
