class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCountMap = {}
        windowCharCount = {}
        
        for s in s1:
            charCountMap[s] = charCountMap.get(s, 0) + 1
        for s in s2:
            charCountMap[s] = charCountMap.get(s, 0)
            windowCharCount[s] = 0
        
        maxWindowIndex = len(s1) - 1
        
        for i in range(len(s2)):
            if i > maxWindowIndex:
                prev_letter = s2[i - 1 - maxWindowIndex]
                windowCharCount[prev_letter] -= 1
                
            windowCharCount[s2[i]] = windowCharCount.get(s2[i], 0) + 1
            if windowCharCount == charCountMap:
                return True
            
        return False
