class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            num = int(a[i]) + int(b[j]) + carry
            
            remainder = num % 2
            carry = num // 2
            res.append(str(remainder))
            j-=1
            i-=1
        while i >= 0:
            num = int(a[i]) + carry
            
            remainder = num % 2
            carry = num // 2
            res.append(str(remainder))
            i-=1
        while j >= 0:
            num = int(b[j]) + carry
            
            remainder = num % 2
            carry = num // 2
            res.append(str(remainder))
            j-=1

        if carry:
            res.append('1')
        
        return "".join(list(reversed(res)))

      