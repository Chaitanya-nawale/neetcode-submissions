class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[low] <= nums[high]:
                return nums[low]
            elif nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1   
        return -1