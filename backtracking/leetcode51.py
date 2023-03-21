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


if __name__ == '__main__':
    solver = Solution()
    params = {
        "n":4,
    }
    print(solver.solveNQueens(**params))
