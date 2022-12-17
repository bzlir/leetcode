'''
https://leetcode.cn/problems/search-insert-position/
'''
class Solution:
    def binary_search_pattern(self, nums, target):
        # Initial
        start_idx, end_idx = 0, len(nums) - 1

        # Binary Search
        while start_idx <= end_idx:
            # update the mid value
            mid = start_idx + (end_idx - start_idx) // 2

            # Contract the search space
            if target < nums[mid]:
                end_idx = mid - 1
            elif target > nums[mid]:
                start_idx = mid + 1
            else:
                return mid
        return start_idx

def binary_search_logn(data, goal, left, right):
    if left > right:
        return left
    mid = left + (right - left) // 2

    if data[mid] == goal:
        return mid
    if goal < data[mid]:
        right = mid - 1
        return binary_search_logn(data, goal, left, right)
    else:
        left = mid + 1
        return binary_search_logn(data, goal, left, right)


if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[1,3,5,6],
        "target": 5,
    }
    print(solver.binary_search_pattern(**params))
