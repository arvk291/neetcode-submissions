class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If character is seen and is inside the current window
            if current_char in char_map and char_map[current_char] >= left:
                # Move left pointer to the right of the previous occurrence
                left = char_map[current_char] + 1
            
            # Update the last seen index of the character
            char_map[current_char] = right
            
            # Calculate current window length and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len   