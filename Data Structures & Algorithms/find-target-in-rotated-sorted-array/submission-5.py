class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
        
            elif nums[mid] > nums[high]:
                # right fold
                if target > nums[mid] or target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # left fold
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1