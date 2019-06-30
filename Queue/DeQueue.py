
class Dequeue:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        l = len(self.items)
        return l

    def show(self):
        print('The Queue is')
        for item in self.items:
            print(item, end=' ')
        print()


def OperateDe():
    q = Dequeue()
    print(q.isEmpty())
    q.addRear(4)
    q.addRear('dog')
    q.addFront('cat')
    q.addFront(True)
    q.show()
    print(q.size())
    q.addFront(8.4)
    q.show()
    q.removeRear()
    q.removeFront()
    q.show()

#OperateDe()
