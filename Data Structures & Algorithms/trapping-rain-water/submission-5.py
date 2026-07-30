class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        lmax, rmax = height[0], height[-1]
        answer = 0
        while left<right:
            if height[left]<height[right]:
                if lmax>height[left]:
                    answer+=lmax-height[left]
                    
                else:
                    lmax = height[left]
                left+=1
            else:
                if rmax>height[right]:
                    answer+=rmax-height[right]
                else:
                    rmax = height[right]
                right-=1
        return answer
