

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        l = len(self.items)
        return l

    def isEmpty(self):
        return self.items == []

    def show(self):
        print('The queue is')
        for i in self.items:
            print(i,end=' ')
        print()


def QueueOps():
    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    q.show()
    print(q.isEmpty())
    print(q.dequeue())
    q.enqueue(8.4)
    q.show()
    print(q.dequeue())
    q.show()

QueueOps()