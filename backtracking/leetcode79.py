class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        path = set()

        def backtrack(row, col, index):
            # accept
            if index == len(word):
                return True
            # reject
            if row < 0 or \
                col < 0 or \
                row >= rows or \
                col >= cols or \
                word[index] != board[row][col] or \
                (row, col) in path:
                return False


            # expand
            path.add((row, col))
            res = backtrack(row+1, col, index+1) or \
                  backtrack(row-1, col, index+1) or \
                  backtrack(row, col+1, index+1) or \
                  backtrack(row, col-1, index+1)
            path.remove((row,col))
            return res



            return res
        

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0): return True
        return False

        

    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "board":[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        "word":"ABCCED"
    }
    print(solver.exist(**params))