class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        low = 1
        result = max_val
        while low <= max_val:
            mid = ((max_val - low) // 2) + low
            curr_count = 0
            for pile in piles:
                curr_count += math.ceil(pile/mid)
            if curr_count <= h:
                result = min(mid, result)
                max_val = mid - 1
            else:
                low = mid + 1
        return result