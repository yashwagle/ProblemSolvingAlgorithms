
class Node:
    def __init__(self, item):
        self.data =item
        self.next = None

    def setData(self, item):
        self.data = item

    def setNext(self, addr):
        self.next = addr

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class Stack:

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n
        self.length = self.length + 1

    def pop(self):
        curr = self.head
        self.head = curr.getNext()
        self.length = self.length - 1
        return curr.getData()

    def peek(self):
        return self.head.getData()

    def display(self):
        curr = self.head
        while curr!=None:
            print(curr.getData())
            curr = curr.getNext()

def driver():
    ch = 0
    s = Stack()
    while ch!='6':
        ch = input('Enter choice 1:push 2:pop 3:peek 4:length 5:display 6:exit')
        if ch=='1':
            item = input('Enter item')
            s.push(item)
        elif ch == '2':
            print('popped item is '+s.pop())
        elif ch=='3':
            print('peeked item is '+s.peek())
        elif ch=='4':
            print('length is '+str(s.length))
        elif ch == '5':
            print('Stack is')
            s.display()

driver()