#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f=[0]*len(nums)
        f[0]=nums[0]
        for i in range(1,len(nums)):
            f[i]=max(f[i-1],0)+nums[i]
        return max(f)
        
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

