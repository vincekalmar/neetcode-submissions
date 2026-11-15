class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0, n-1

        while l <= r:

            sm = numbers[l] + numbers[r]

            if sm > target:
                r-=1
            elif sm < target:
                l+=1
            else:
                return [l+1, r+1]

                