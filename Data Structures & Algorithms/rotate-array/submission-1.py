class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        k %= n
        first = True
        prev = nums[0]
        count = 0
        start = 0
        while count < n:
            i = (i+ k) % n
            curr = nums[i]
            nums[i] = prev
            prev = curr
            if i == start:
                i = (i+1) % n
                start = i
                prev = nums[start]
            count +=1

        nums[i] = prev

        




       