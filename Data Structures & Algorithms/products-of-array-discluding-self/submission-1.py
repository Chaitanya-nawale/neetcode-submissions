class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplication = 1
        zero_index = -1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if zero_index != -1:
                    return [0]* len(nums)
                zero_index = i
                continue
            multiplication *= num
        if zero_index != -1:
            result = [0]* len(nums)
            result[zero_index] = multiplication
            return result
        result = [int(multiplication /num) for num in nums]       
        return result