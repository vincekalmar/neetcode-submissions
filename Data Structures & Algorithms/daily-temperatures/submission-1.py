class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, index 
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                t, i = stack.pop()
                res[i] = index - i
            
            stack.append((temp, index))

        return res
        
        # (30, 0 
        # 0 0
