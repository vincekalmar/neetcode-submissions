class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for token in operations:
            print(stack)
            if token == '+':
                left, right = stack.pop(), stack.pop()
                stack.append(right)
                stack.append(left)
                stack.append(left + right)
            elif token == 'D':
                left = stack.pop()
                stack.append(left)
                stack.append(left*2)

            elif token == 'C':
                stack.pop()

            else:
                stack.append(int(token))
        
        return sum(stack)

