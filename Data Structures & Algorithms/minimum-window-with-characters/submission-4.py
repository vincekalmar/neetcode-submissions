class Solution:
    def minWindow(self, s: str, t: str) -> str:

        targetCount = Counter(t)
        currCount = defaultdict(int)

        incorrectCount = len(t)

        l = 0

        minWindow = (0,0)
        minWindowLen = float('inf')
        for r, c in enumerate(s):

            if c in targetCount:
                currCount[c] += 1
                if currCount[c] <= targetCount[c]:
                    incorrectCount -= 1
            
            while incorrectCount == 0:
                currWindow = r - l + 1
                if s[l] in currCount:
                    currCount[s[l]] -= 1
                
                    if currCount[s[l]] < targetCount[s[l]]:
                        incorrectCount += 1       

                if currWindow < minWindowLen:
                    minWindowLen = currWindow
                    minWindow = (l,r)

                l += 1

        if minWindowLen == float('inf'):
            return ""        
        left, right = minWindow

        return s[left:right+1]





                