class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = high // 2
        while low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                print(high)
            else:
                low = mid + 1
                print(low)
            mid = ((high - low) // 2) + low
        return -1