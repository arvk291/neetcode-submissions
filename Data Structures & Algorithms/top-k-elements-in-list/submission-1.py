class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        else:
            num_counts = Counter(nums)
            sorted_vals = sorted(num_counts.values())[-k:]
            return [ k for k,v in num_counts.items() if v in sorted_vals]

