class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        slow = fast = nums[0] #1, 1
        firstRun = True
        while firstRun or slow != fast:
            slow = nums[slow] #
            fast = nums[nums[fast]] #1
            firstRun = False

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow