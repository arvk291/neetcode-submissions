class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)-1
        while right<len(s2):
            window = s2[left:right+1]
            if sorted(window) == sorted(s1):
                return True
            else:
                left+=1
                right+=1
        return False