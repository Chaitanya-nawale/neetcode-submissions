class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_char_map = {}
        s_char_map = {}
        min_str = ""
        min_str_len = len(s) + 1

        for letter in t:
            t_char_map[letter] = t_char_map.get(letter,0) + 1
            s_char_map[letter] = s_char_map.get(letter,0)
        
        l, r = 0, 0

        while(r < len(s)):
            letter = s[r]
            t_char_map[letter] = t_char_map.get(letter,0)
            s_char_map[letter] = s_char_map.get(letter,0) + 1
            matched = True
            for key in t_char_map:
                if t_char_map[key] > s_char_map[key]:
                    matched = False
                    break
            if matched is True:
                while(l <=r):
                    letter_removed = s[l]
                    if t_char_map[letter_removed] > (s_char_map[letter_removed] - 1):
                        s_char_map[letter_removed] = s_char_map[letter_removed] - 1
                        if len(s[l:r+1]) < min_str_len:
                            min_str = s[l:r+1]
                            min_str_len = len(min_str)
                        l += 1
                        break
                    l += 1
                    s_char_map[letter_removed] = s_char_map[letter_removed] - 1     
            r+=1
        return min_str