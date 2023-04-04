class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return False

        nums = sorted(nums)
        tmp = nums[0]
        for i in range(1,n):
            if tmp == nums[i]: return True
            tmp = nums[i]
        return False
    
    def containsDuplicate_by_gpt(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[1,2,3,1],
    }
    print(solver.containsDuplicate(**params))