class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for index, num in enumerate(nums):
            output.append(math.prod(nums[:index]+nums[index+1:]))
        return output
        