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

def checkParamsAll(Exp):
    s = Stack()
    i = 0
    balanced = True
    symbol
    while i < len(str) and balanced == True:
        if str[i] == '(' or str[i] == '{' or str[i] == '[':
            s.push(str[i])
        else:
            symbol = s.pop()
            if s.isEmpty():
                balanced = False
            elif str[i] == '}' and symbol != '{':
                balanced = False
            elif str[i] == ')' and symbol != '(':
                balanced = False
            elif str[i] == ']' and symbol != '[':
                balanced = False
        i = i + 1

    if balanced == False or s.isEmpty() == True:
        return False
    return True



print(checkBalancedParams('((()()())()))('))


