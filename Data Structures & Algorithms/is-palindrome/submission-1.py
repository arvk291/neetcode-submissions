import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = re.sub(r'[\W_]+', '', s)
        l_pointer, r_pointer = 0, len(clean_string)-1
        while l_pointer<r_pointer:
            if clean_string[l_pointer].lower() != clean_string[r_pointer].lower():
                return False
            l_pointer+=1
            r_pointer-=1
        return True