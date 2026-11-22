class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero = one = 0

        for two, num in enumerate(nums):
            temp = num
            nums[two] = 2
            if temp < 2:
                nums[one] = 1
                one += 1
            if temp < 1:
                nums[zero] = 0
                zero += 1
        

