class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open, close = 0, 0

        for char in s:

            if char == '(':
                open += 1
                close += 1
            
            if char == ')':
                open -= 1
                close -= 1
            
            if char == '*':
                open -= 1
                close += 1

            if open < 0:
                open = 0
            
            if close < 0:
                return False
        
        return open == 0
