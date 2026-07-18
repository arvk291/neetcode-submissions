class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, 1
        while left < right and right < len(nums):
            if nums[right] > nums[left]:
                left+=1
                right+=1
            else:
                return nums[right]
        return nums[0]