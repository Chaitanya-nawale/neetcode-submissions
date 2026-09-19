class Solution:
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        index = 0
        while low <= high:
            mid = ((high - low) // 2) + low
            matrix[mid][0]
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target and ( (mid == len(matrix) - 1 ) or (matrix[mid + 1][0] > target ) ):
                index = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        nums = matrix[index]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = ((high - low) // 2) + low
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False