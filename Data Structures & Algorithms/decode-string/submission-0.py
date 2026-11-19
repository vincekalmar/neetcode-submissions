class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for i, token in enumerate(s):
            if token == ']':
                sub = ""
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                num = int(num)

                sub = sub * num
                stack.append(sub)
            else:
                stack.append(token)

        return "".join(stack)

