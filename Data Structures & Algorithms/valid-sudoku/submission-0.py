class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hash1(i,j):
            return i
        def hash2(i,j):
            return j
        def hash3(i,j):
            return (i//3,j//3)
        
        count1 = defaultdict(lambda:defaultdict(bool))
        count2 = defaultdict(lambda:defaultdict(bool))
        count3 = defaultdict(lambda:defaultdict(bool))

        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val=='.':
                    continue
                if count1[hash1(i,j)][val] or count2[hash2(i,j)][val]  or count3[hash3(i,j)][val] :
                    print(i,j,count1,count2,count3)
                    return False
                count1[hash1(i,j)][val]=True
                count2[hash2(i,j)][val]=True
                count3[hash3(i,j)][val]=True
        return True
