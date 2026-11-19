class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')

        stack = []

        print(path)
        for token in path:
            if token == '..':
                if stack:
                    stack.pop()
            elif token == '' or token == '.':
                continue
            else:
                stack.append(token)

        return '/' + '/'.join(stack)

        
