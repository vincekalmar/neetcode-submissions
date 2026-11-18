class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    

        total = nums[0]

        res = nums[0]
        for i, num in enumerate(nums[1:]):
            if total < 0:
                total = 0
            total += num
            res = max(total, res)
            


        return res
            
