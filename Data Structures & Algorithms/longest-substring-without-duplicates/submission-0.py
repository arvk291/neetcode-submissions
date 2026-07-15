class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, window = 0, ""
        left = 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left+=1
            window = s[left:right+1]
            ans = max(ans, len(window))
        return ans


        