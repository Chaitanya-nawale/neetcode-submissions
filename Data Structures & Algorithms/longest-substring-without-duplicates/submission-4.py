class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_to_index_map = {}
        l = 0
        for i, character in enumerate(s):
            if ord(character) in char_to_index_map:
                prev_occur = char_to_index_map.get(ord(character))
                if prev_occur >= l:
                    max_len = max(max_len, i - l)
                    l = prev_occur + 1
            char_to_index_map[ord(character)] = i
        max_len = max(max_len, len(s) - l)
        return max_len
