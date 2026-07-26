class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i
            stack.append(i)
        res = [x - i if x > 0 else 0 for i, x in enumerate(res)]
        return res