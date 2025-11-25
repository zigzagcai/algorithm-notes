#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import inf


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n=len(nums)
        # fmax=[0]*n
        # fmin=[0]*n
        # fmax[0]=nums[0]
        # fmin[0]=nums[0]
        # for i in range(1,n):
        #     x=nums[i]
        #     fmax[i]=max(fmax[i-1]*x,fmin[i-1]*x,x)
        #     fmin[i]=min(fmax[i-1]*x,fmin[i-1]*x,x)
        # return max(fmax)
        fmax=fmin=1
        ans=-inf
        for x in nums:
            fmax, fmin=max(fmax*x,fmin*x,x), min(fmax*x,fmin*x,x)
            ans=max(ans,fmax)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#

