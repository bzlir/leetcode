

class Solution(object):

    def letterCombinations(self, digits):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not digits:
            return []
        
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        res = []
        n = len(digits)
        def backtrack(p, curStr):
            m = len(curStr)
            if m == n:
                res.append(curStr)
                return
            for letter in mapping[digits[p]]:
                backtrack(p+1,curStr+letter)
            return res
        

        backtrack(0,"")
        return res

    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "digits":"23",
    }
    print(solver.letterCombinations(**params))