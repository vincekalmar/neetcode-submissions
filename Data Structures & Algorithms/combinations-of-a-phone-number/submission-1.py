class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mp = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }


        res = []

        def dfs(start, combo):
            if start == len(digits):
                res.append("".join(combo))
                return

            
            letters = mp[digits[start]]
            for char in letters:
                combo.append(char)
                dfs(start+1, combo)
                combo.pop()

        dfs(0,[])


        return res if res != [""] else []



    
                