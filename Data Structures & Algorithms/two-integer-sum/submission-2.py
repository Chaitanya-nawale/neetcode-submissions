class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        multimap = defaultdict(list)
        for i in range(0, len(nums)):
            multimap[nums[i]].append(i)
        
        for i in range(0, len(nums)):
            targetList = multimap[target - nums[i]]
            if targetList:
                if target - nums[i] != nums[i] or len(targetList)>1:
                    return [i, multimap[target - nums[i]][-1]]