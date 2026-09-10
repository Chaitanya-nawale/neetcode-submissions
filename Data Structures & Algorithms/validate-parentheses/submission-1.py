class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{": "}", "(": ")", "[": "]"}
        for character in s:
            if character in ["{", "[", "("]:
                stack.append(character)
            elif len(stack) == 0:
                return False
            else:
                returned = stack.pop()
                if brackets[returned] != character:
                    return False
        if len(stack) !=0:
            return False
        return True