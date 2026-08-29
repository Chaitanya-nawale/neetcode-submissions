class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons_num_start = {}
        cons_num_end = {}
        checked_values = set()
        for num in nums:
            if num in checked_values:
                continue
            if num - 1 in cons_num_end:
                if num + 1 in cons_num_start:
                    old_end_value = cons_num_start.pop(num + 1)
                    old_start_value = cons_num_end.pop(num - 1)
                    cons_num_start[old_start_value] = old_end_value
                    cons_num_end[old_end_value] = old_start_value
                else:
                    prev_cons_start = cons_num_end.pop(num - 1)
                    cons_num_start[prev_cons_start] = num
                    cons_num_end[num] = prev_cons_start
            elif num + 1 in cons_num_start:
                old_value = cons_num_start.pop(num + 1)
                cons_num_start[num] = old_value
                cons_num_end[old_value] = num
            else:
                cons_num_start[num] = num
                cons_num_end[num] = num
            checked_values.add(num)
        max_range = 0
        for start, end in cons_num_start.items():
            num_range = end - start +1
            if max_range < num_range:
                max_range = num_range
        return max_range
        