class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            diff = target-num
            if diff in nums[index+1:]:
                return [index, nums[index+1:].index(diff)+index+1]