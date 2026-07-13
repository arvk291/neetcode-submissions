class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0,1
        while right< len(numbers) and left<right:
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif right==len(numbers)-1 and right-left>1:
                right = left+2
                left+=1
                
            else:
                right+=1
        




        