class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_array = sorted(nums1 + nums2)
        mid = (len(combined_array)-1)//2
        if len(combined_array)%2 == 0:
            return (combined_array[mid]+combined_array[mid+1])/2
        else:
            return combined_array[mid]