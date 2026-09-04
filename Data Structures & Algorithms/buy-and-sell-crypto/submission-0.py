class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_price = 101
        biggest_price = 0
        max_diff = 0
        for curr_price in prices:
            if curr_price < smallest_price:
                max_diff = max(max_diff, biggest_price  -smallest_price)
                smallest_price = curr_price
                biggest_price = curr_price
            if curr_price > biggest_price:
                biggest_price = curr_price
        max_diff = max(max_diff, biggest_price  -smallest_price)
        return max_diff