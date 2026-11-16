class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        l = 0
        mp = {}
        res = 0

        # p w w k e w
        #   l
        #     r
        # mp = {p:0, w: 2, k:3, e:3, }
        # res = 2
        for r, c in enumerate(s):

            if c in mp:
                l = max(l, mp[c]+1)
            
            res = max(r-l+1, res)
            mp[c] = r

        return res
