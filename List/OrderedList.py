
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

    def getdata(self):
        return self.data

    def setdata(self, item):
        self.data = item

    def setNext(self, add):
        self.next = add

    def getNext(self):
        return self.next


class OrderedList:

    def __init__(self):
        self.head = None

    def insert(self, item):
        n = Node(item)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            prev = None
            if item < curr.getdata():
                n.setNext(curr)
                self.head = n
                return
            while curr!= None and item > curr.getdata():
                prev = curr
                curr = curr.getNext()
            if curr == None:
                prev.setNext(n)
            else:
                n.setNext(curr)
                prev.setNext(n)

    def show(self):
        curr = self.head
        print('The list is')
        while curr != None:
            print(curr.getdata(),end=' ')
            curr = curr.getNext()
        print()

    def search(self, item):
        curr = self.head
        if item < curr.getdata():
            return False
        Found = False
        while curr!=None and not Found:
            if curr.getdata() == item:
                Found = True
            elif item < curr.getdata():
                Found= False
                break
            curr = curr.getNext()
        return Found




def driver():
    on = OrderedList()
    on.insert(5)
    on.insert(2)
    on.insert(9)
    on.insert(-1)
    on.insert(100)
    on.insert(4)
    on.show()
    print(on.search(-1))
    print(on.search(101))



driver()
