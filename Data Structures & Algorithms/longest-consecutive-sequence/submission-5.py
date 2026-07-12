import numpy as np
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            seq = 1
            sorted_nums = sorted(set(nums))
            left, right = 0, 1
            seq_res = []
            while right<len(sorted_nums):
                if np.abs(sorted_nums[right] - sorted_nums[left]) == 1:
                    left+=1
                    right+=1
                    seq+=1
                else:
                    seq_res.append(seq)
                    left=right
                    right+=1
                    seq=1
            seq_res.append(seq)
            return max(seq_res)