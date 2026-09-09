class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if nums == []:
            return result
        from sortedcontainers import SortedList

        left = 0
        highest = nums[0]
        highest_index = 0

        sliding_window = SortedList(nums[:k])
        
        result.append(sliding_window[-1])

        for i in range(k, len(nums)):
            sliding_window.add(nums[i])
            sliding_window.remove(nums[i-k])
            result.append(sliding_window[-1])

        return result