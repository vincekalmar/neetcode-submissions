class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
       # 2, 3, 8, 9, 14

       # total = 14 l = 0, 12, l = 1, 9 l = 2

        l = 0
        total = 0 
        res = float('inf')
        for r, num in enumerate(nums):
            total += num

            if total >= target:
                res = min(r-l+1, res)

                while total - nums[l] >= target:
                    total -= nums[l]
                    l+=1
                
                res = min(r-l+1, res)
        
        return res if res != float('inf') else 0

