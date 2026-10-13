class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dups = [0] * len(nums)
        for num in nums:
            if dups[num]:
                return num
            else:
                dups[num] = 1 
        return 0