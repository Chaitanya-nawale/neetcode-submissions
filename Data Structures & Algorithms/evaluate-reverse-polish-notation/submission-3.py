class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        print(ops)
        for token in tokens:
            if token in ops:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if token == "+":
                    stack.append(first_operand + second_operand)
                elif token == "-":
                    stack.append(first_operand - second_operand)
                elif token == "*":
                    stack.append(first_operand * second_operand)
                else:
                    if (first_operand < 0 or second_operand < 0 ) and first_operand % second_operand != 0 and not (first_operand < 0 and second_operand < 0 ):
                        stack.append((first_operand // second_operand)+1)
                    else:
                        stack.append(first_operand // second_operand)
            else:
                stack.append(int(token))
        return stack.pop()