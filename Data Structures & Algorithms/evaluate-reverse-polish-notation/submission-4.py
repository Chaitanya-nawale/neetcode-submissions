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
                    stack.append(int(first_operand / second_operand))
            else:
                stack.append(int(token))
        return stack.pop()