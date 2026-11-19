class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            if token == '+':
                left, right = stack.pop(), stack.pop()
                stack.append(left+right)
            elif token == '-':
                left, right = stack.pop(), stack.pop()
                stack.append(right-left)
            elif token == '*':
                left, right = stack.pop(), stack.pop()
                stack.append(left*right)
            elif token == '/':
                left, right = stack.pop(), stack.pop()
                stack.append(int(right/left))
            else:
                stack.append(int(token))



        return stack.pop()

