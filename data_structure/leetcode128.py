class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        res = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                res = max(length, res)

        return res
    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[100,4,200,1,3,2],
    }
    print(solver.longestConsecutive(**params))