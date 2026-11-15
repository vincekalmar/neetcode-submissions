class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        total = 1
        for i, num in enumerate(nums):
            total *= num
            prefix.append(total)

        total = 1
        postfix = [0] * len(nums) 
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            postfix[i] = total

        res = [1] * len(nums)
  
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res

            #1 2 8 48

           # 48 48 24 6 




            