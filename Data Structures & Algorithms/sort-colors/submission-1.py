class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero = one = 0

        for two in range(len(nums)):
            temp = nums[two]
            nums[two] = 2

            if temp < 2:
                nums[one] = 1
                one+=1
   
            if temp < 1:
                nums[zero] = 0
                zero += 1         

       # 1, 0, 1, 2
      #  0, 2
       #    z
      #     o
      #     t
        