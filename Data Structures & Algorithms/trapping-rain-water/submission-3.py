from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        max_area = 0
        
        while left < right:
            # Update the max heights seen so far
            if height[left] >= left_max:
                left_max = height[left]
            else:
                # If current height is less than left_max, water can be trapped
                # The water level is determined by left_max (since left_max < right_max)
                max_area += left_max - height[left]
            
            if height[right] >= right_max:
                right_max = height[right]
            else:
                # If current height is less than right_max, water can be trapped
                # The water level is determined by right_max (since right_max <= left_max)
                max_area += right_max - height[right]
            
            # Move the pointer with the smaller max height
            # This ensures we are always processing the side that limits the water level
            if left_max < right_max:
                left += 1
            else:
                right -= 1
                
        return max_area