class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # temp, daySeen
        res = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                t, d = stack.pop()
                res[d] = day - d
            stack.append((temp, day))
        
        return res

