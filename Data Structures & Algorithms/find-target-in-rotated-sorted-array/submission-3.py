class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = ((high - low) // 2) + low
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[high]:
                print("sorted", nums[low:high+1])
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] > nums[high]:
                # right fold
                if target > nums[mid]:
                    low = mid + 1
                elif target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # left fold
                if target < nums[mid]:
                    high = mid - 1
                elif target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1