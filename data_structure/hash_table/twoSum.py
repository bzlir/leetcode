'''
https://leetcode.cn/problems/two-sum
'''
class Solution:
    def hash_table_pattern(self, nums, target):
        # Initial
        hash_table = dict()
        for idx, val in enumerate(nums):
            if target - val in hash_table:
                return [hash_table[target - val], idx]
            hash_table[val] = idx
        
        return []


if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums": [3,2,4],
        "target": 6
    }
    print(solver.hash_table_pattern(**params))
