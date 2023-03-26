class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        # n = len(nums)
        # def backtrack(path, choices):
        def backtrack(path, xy_diff, xy_sum):
            m = len(path)
            if m == n:
                # res.append(list(path))
                res.append(path)
                return
            # for item in choices:
            for item in range(n):
                if item not in path and m - item not in xy_diff and m + item not in xy_sum:
                # if item in path:
                    # continue
                # path.append(item)
                # backtrack(path,choices)
                    backtrack(path+[item],xy_diff | {m-item}, xy_sum | {m+item})
                # path.pop()
            # return res
        
        # backtrack([],nums)
        backtrack([],set(),set())
        return [['.'*i+'Q'+'.'*(n-i-1)for i in queen]for queen in res]

    def solveNQueens2(self,n):
        res = []
        def backtrack(nums, row):
            if row == n:
                res.append(nums[:])
                return
            for col in range(n):
                nums[row] = col
                if valid(nums, row):
                    backtrack(nums, row+1)
        
        def valid(nums,row):
            for i in range(row):
                if abs(nums[i]-nums[row]) == abs(row-i) or nums[i] == nums[row]:
                    return False 
            return True
        
        backtrack([None for _ in range(n)],0)

        result = [[] for _ in range(len(res))]
        for i in range(len(res)):
            for col in res[i]:
                tmp = '.'*n
                result[i].append(tmp[:col]+'Q'+tmp[col+1:])
        return result


    def solveNQueens3(self,n):
        result = []
        board = [['.']*n for _ in range(n)]
        cols = set()
        negDiag = set()
        posDiag = set()

        def dfs(row):
            # accept
            if row == n:
                rep_board = [''.join(r) for r in board]
                result.append(rep_board)
                return 
            # expand
            for col in range(n):
                # purning
                ## 1 同一列放过
                ## 2 同对角线放过
                ### 2.1 左对角线冲突
                ### 2.2 右对角线冲突
                if col in cols or \
                    (row - col) in negDiag or \
                    (row + col) in posDiag:
                    continue
                
                cols.add(col)
                negDiag.add(row-col)
                posDiag.add(row+col)
                board[row][col] = 'Q'

                dfs(row + 1)

                cols.remove(col)
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                board[row][col] = '.'
                
                          
        dfs(0)
        return result
if __name__ == '__main__':
    solver = Solution()
    params = {
        "n":4,
    }
    print(solver.solveNQueens3(**params))
