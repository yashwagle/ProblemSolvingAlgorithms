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
    symbol = ''
    while i < len(Exp) and balanced == True:
        if Exp[i] == '(' or Exp[i] == '{' or Exp[i] == '[':
            s.push(Exp[i])
        else:
            if s.isEmpty():
                balanced = False
            symbol = s.pop()
            if Exp[i] == '}' and symbol != '{':
                balanced = False
            elif Exp[i] == ')' and symbol != '(':
                balanced = False
            elif Exp[i] == ']' and symbol != '[':
                balanced = False
        i = i + 1
    if balanced == False or s.isEmpty() == False:
        return False
    return True



print(checkParamsAll('[{()]'))


