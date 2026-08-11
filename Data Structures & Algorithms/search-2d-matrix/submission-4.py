def bin_search(arr, target):
    left,right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0,m):
            if target <= matrix[i][-1] and target >=matrix[i][0]:
                return bin_search(matrix[i], target)
        return False
        