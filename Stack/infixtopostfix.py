from Stack import Stack


def ConvertInfixtoPostfix(exp):
    s = Stack()
    expList = exp.split()
    OperatorPrec = {}
    OperatorPrec['+'] = 2
    OperatorPrec['-'] = 2
    OperatorPrec['*'] = 3
    OperatorPrec['/'] = 3
    OperatorPrec['('] = 0
    OperatorPrec[')'] = 0
    postfix = []
    for ch in expList:
        if ch not in OperatorPrec:
            postfix.append(ch)
        else:
            if ch == '(':
                s.push('(')
            elif ch == ')':
                topToken = s.pop()
                while topToken != '(':
                    postfix.append(topToken)
                    topToken = s.pop()
            elif s.isEmpty():
                s.push(ch)
            elif OperatorPrec[ch] > OperatorPrec[s.peek()]:
                s.push(ch)
            else:
                while s.isEmpty() == False and OperatorPrec[s.peek()] >= OperatorPrec[ch]:
                    postfix.append(s.pop())
                s.push(ch)
    while s.isEmpty() == False:
        postfix.append(s.pop())
    return postfix

def evaluatePostfix(postfixList):
    st = Stack()
    for ch in postfixList:
        if ch in '0123456789':
            st.push(ch)
        else:
            operand2 = st.pop()
            operand1 = st.pop()
            if ch == '+':
                ans = int(operand1) + int(operand2)
            elif ch == '-':
                ans = int(operand1) - int(operand2)
            elif ch == '*':
                ans = int(operand1) * int(operand2)
            elif ch == '/':
                ans = int(operand1) // int(operand2)
            st.push(ans)
    return st.pop()


print((evaluatePostfix(ConvertInfixtoPostfix('( 9 + 2 ) * 8'))))


