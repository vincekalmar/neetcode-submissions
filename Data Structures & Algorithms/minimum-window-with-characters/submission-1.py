class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        targetCount = Counter(t)
        subCount = defaultdict(int)
        
        res = ""

        incorrectCount = len(t)

        for r, char in enumerate(s):
            if char in targetCount:
                subCount[char] += 1
                if subCount[char] <= targetCount[char]:
                    incorrectCount -= 1
            
            while incorrectCount == 0:
                currentSubstring = s[l:r+1]
                if res == "" or len(res) > len(currentSubstring):
                    res = currentSubstring
                leftChar = s[l]
                if leftChar in subCount: 
                    subCount[leftChar] -= 1
                
                    if subCount[leftChar] < targetCount[leftChar]:
                        incorrectCount += 1

                l+=1


        return res
                 
                    

                
                
            

            

