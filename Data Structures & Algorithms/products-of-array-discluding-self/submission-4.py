class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        total = 1
        for num in nums:
            total *= num
            prefix.append(total)
        prefix.append(1)

        postfix = [1]
        total = 1
        for num in reversed(nums):
            total *= num
            postfix.append(total)

        postfix = list(reversed(postfix))

       # pre: 1  2  8  48
        # post 48 48 24  6

        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = postfix[i+1] * prefix[i-1]
        
        return res








    