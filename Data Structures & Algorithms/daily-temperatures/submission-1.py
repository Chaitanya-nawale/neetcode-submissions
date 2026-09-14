class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                prev_index = stack.pop()[1]
                results[prev_index] = i - prev_index
            stack.append((temperatures[i],i))
        return results