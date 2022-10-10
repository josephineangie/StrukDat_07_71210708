class PrefixConverter:
    def __init__(self):
        self.stackList = []

    # method untuk menambahkan data baru
    def push(self, data):
        self.stackList.append(data)

    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus data paling atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    def cekValidExpression(self, expression, x):
        if x in "+-":
            return 1
        elif x in "*/":
            return 2
        elif x in "^":
            return 3
        return 0

    def infixToPrefix(self, expression, A):
        stack = PrefixConverter()
        A = '(' + A + ')'
        output = ""
        for c in A[::-1]:
            print(c)
            if c.isnumeric():
                output += c
            elif c == ")":
                stack.push(c)
            elif c in "+-*/^":
                if c == "^":
                    while cekValidExpression(c) <= cekValidExpression(stack.top()):
                        output += stack.pop()
                else:
                    while cekValidExpression(c) < cekValidExpression(stack.top()):
                        output += stack.pop()
                stack.push(c)
            elif c == "(":
                while not stack.is_empty():
                    c1 = stack.pop()
                    if c1 == ')':
                        break
                    output += c1
        while not stack.is_empty():
            output += stack.pop()
        return output
        # prefiks = " "
        # print ("Ekspresi Prefix-nya Adalah: ")
        # for i in
        # # Tuliskan code anda disini
        # operators = []
        # operands = []

        # for i in range(len(infix)):

        #     if (infix[i] == '(' ):
        #         operators.append(infix[i])

        #     elif (infix[i] == ')'):
        #         while (len(operators)!=0 and (operators[-1] != '(' )):
        #             op1 = operands[-1]
        #             operands.pop()
        #             op2 = operands[-1]
        #             operands.pop()
        #             op = operators[-1]
        #             operators.pop()
        #             tmp = op + op2 + op1
        #             operands.append(tmp)
        #         operators.pop()
        #     elif (not isOperator(infix[i])):
        #         operands.append(infix[i] + "")
        #     else:
        #         while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
        #             op1 = operands[-1]
        #             operands.pop()

        #             op2 = operands[-1]
        #             operands.pop()

        #             op = operators[-1]
        #             operators.pop()

        #             tmp = op + op2 + op1
        #             operands.append(tmp)
        #         operators.append(infix[i])

        # while (len(operators)!=0):
        #     op1 = operands[-1]
        #     operands.pop()

        #     op2 = operands[-1]
        #     operands.pop()

        #     op = operators[-1]
        #     operators.pop()

        #     tmp = op + op2 + op1
        #     operands.append(tmp)
        # return operands[-1]


# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
