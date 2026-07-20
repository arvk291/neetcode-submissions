class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left, right = 0, len(heights)-1
        while left < right:
            max_water = max(max_water, min(heights[left], heights[right]) * (right - left))
            if right == left+1:
                left+=1
                right = len(heights)-1
            else:
                right-=1
        return max_water

        