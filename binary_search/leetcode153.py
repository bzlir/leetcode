class Solution(object):
    def findMin(self, nums):
        res = nums[0]

        l, r = 0, len(nums) - 1


        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            m = (l+r)>>1
            res = min(nums[m],res)
            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return res
    
    def findMin2(self,nums):
        res = nums[0]
        if len(nums) == 1:
            return res
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i-1]:
                res = min(res, nums[i])
        
        res = min(res,nums[-1])
        return res
