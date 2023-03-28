class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[100,4,200,1,3,2],
    }
    print(solver.longestConsecutive(**params))