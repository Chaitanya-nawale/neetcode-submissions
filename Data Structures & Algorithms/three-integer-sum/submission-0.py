class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        nums.sort()
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            j = i+1
            k = len(nums)-1
            while(j<k):
                sum = nums[j] + nums[k]
                if target > sum:
                    j += 1
                elif target < sum:
                    k -= 1
                else:
                    result_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return [ list(result) for result in result_set ]