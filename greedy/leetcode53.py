class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub
    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[-2,1,-3,4,-1,2,1,-5,4],
    }
    print(solver.maxSubArray(**params))