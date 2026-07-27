import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right  # Initialize with the maximum possible speed
        
        while left <= right:
            mid = (left + right) // 2
            # Calculate total hours needed at speed 'mid'
            # Use the original 'piles' list, not a range
            total_hours = sum(math.ceil(pile / mid) for pile in piles)
            
            if total_hours <= h:
                answer = mid  # This speed works, try smaller
                right = mid - 1
            else:
                left = mid + 1  # Too slow, need higher speed
        
        return answer   