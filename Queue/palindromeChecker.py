from DeQueue import Dequeue


def checkpalindrome(str):
    d = Dequeue()
    str = str.replace(' ','')
    for ch in str:
        d.addFront(ch)

    ispalindrome = True
    while d.size() > 1 and ispalindrome:
        if d.removeFront() != d.removeRear():
            ispalindrome = False
    return ispalindrome

print(checkpalindrome('I PREFER DI'))