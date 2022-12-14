'''
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
import bisect
class Solution:
    def binary_search(self, nums, target):
        # Inital
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left == right:
            return [-1, -1]
        return [left, right - 1]


if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums": [5,7,7,8,8,10],
        "target":8
    }
    print(solver.binary_search(**params))
