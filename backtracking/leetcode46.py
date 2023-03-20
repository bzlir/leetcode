from collections import Counter

class Solution(object):



    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # exit condition
            if first == n:
                # add result
                output.append(nums[:])
            # select
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack()
        return output
    
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def backtrack(path, choices):
            m = len(path)
            if m == n:
                res.append(list(path))
                return
            for item in choices:
                if item in path:
                    continue
                path.append(item)
                backtrack(path,choices)
                path.pop()
            return res
        

        backtrack([],nums)
        return res
    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[1,2,3],
    }
    print(solver.permute2(**params))