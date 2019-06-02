class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def show(self):
        print('stack is ')
        n = len(self.items) - 1
        while n >= 0:
            print(self.items[n])
            n = n-1




