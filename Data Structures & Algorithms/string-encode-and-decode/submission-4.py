class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s

        return res

    def decode(self, s: str) -> List[str]:
       
        r = 0
        res = []
        while r < len(s):
            l=r
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])

        return res



            
       

            


            

