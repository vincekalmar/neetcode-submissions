class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]

        for i in range(len(res)):
            for s in strs:
                if i >= len(s) or res[i] != s[i]:
                    return s[:i]
        
        return res
            
            


            