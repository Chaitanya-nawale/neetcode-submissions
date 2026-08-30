class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1
        sum_num = 0
        while(i<j):
            sum_num = numbers[i]+ numbers[j]
            if target == sum_num:
                return [i+1, j+1]
            elif target < sum_num:
                j -= 1
            else:
                i += 1
        return [1,2]
