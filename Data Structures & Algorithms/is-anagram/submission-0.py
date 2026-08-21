class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_multiset = Counter(s)
        t_multiset = Counter(t)
        print(s_multiset)
        print(t_multiset)
        print(s_multiset == t_multiset)
        return s_multiset == t_multiset
        