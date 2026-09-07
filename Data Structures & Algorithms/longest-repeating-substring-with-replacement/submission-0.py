class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(65,91):
            curr_letter = chr(i)
            temp = deque(maxlen = k+1)
            temp.append(0)
            for i, letter in enumerate(s):
                if letter != curr_letter:
                    temp.append(i+1)
                max_len = max(max_len, i + 1  - temp[0])    
        return max_len