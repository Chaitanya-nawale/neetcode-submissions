class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMapping = {}
        
        for string in strs:
            my_dict = dict(Counter(string))
            sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
            key = str(sorted_dict)
            value = anagramMapping.get(key, [])
            value.append(string)
            anagramMapping[key] = value
        return [val for val in anagramMapping.values()]
        