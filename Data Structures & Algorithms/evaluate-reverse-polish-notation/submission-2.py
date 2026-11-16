class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i, token in enumerate(tokens):

            if token == '*':
                right = stack.pop()
                left = stack.pop()

                stack.append(left * right)
            elif token == '/':
                right = stack.pop()
                left = stack.pop()

                stack.append(int(left / right))
          
            elif token == '-':
                right = stack.pop()
                left = stack.pop()

                stack.append(left - right)
            elif token == '+':
                right = stack.pop()
                left = stack.pop()

                stack.append(left + right)
            else:

                stack.append(int(token))

        return stack[0]
            