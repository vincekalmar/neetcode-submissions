class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            
            if c in mp:
                l = max(mp[c] + 1, l)
                
            res = max(r - l + 1, res)
            mp[c] = r

        return res