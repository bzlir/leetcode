class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx - 1] == val:
                continue
            l, r =  idx + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
    

if __name__ == '__main__':
    solver = Solution()
    params = {
        "nums":[-1,0,1,2,-1,-4],
    }
    print(solver.threeSum(**params))