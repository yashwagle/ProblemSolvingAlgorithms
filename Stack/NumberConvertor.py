from Stack import Stack


def convertToBinary(num):
    s = Stack()
    while num > 0:
        r = num % 2
        s.push(r)
        num = num // 2

    binary = ""
    while s.isEmpty() == False:
        binary = binary+str(s.pop())

    return binary

def convertToBase(num, base):
    chars='0123456789ABCDEF'
    s = Stack()
    while num > 0 :
        r = num % base
        s.push(chars[r])
        num = num // base
    num = ""
    while s.isEmpty() == False:
        num = num + s.pop()
    return num

print(hex(89),convertToBase(89,16))

