class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1


        def backtrack():
            # accept
            if len(perm) == len(nums):
                res.append(list(perm))
                return 
            
            # brute force expand
            for n in nums:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -=1
                    backtrack()
                    count[n] +=1
                    perm.pop()


        backtrack()
        return res
    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[1,1,2],
    }
    print(solver.permuteUnique(**params))