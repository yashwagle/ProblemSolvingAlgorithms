from Stack import Stack


def checkBalancedParams(str):
    s = Stack()
    i = 0
    balanced = True
    while i < len(str) and balanced == True:
        if str[i] == '(':
            s.push('(')
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        i = i+1

    if balanced == False or s.isEmpty() == False:
        return False
    return True


print(checkBalancedParams('((()()())()))('))


