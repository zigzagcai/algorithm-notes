#
# @lc app=leetcode.cn id=312 lang=python3
# @lcpr version=30204
#
# [312] 戳气球
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        dp = [[0]*len(nums) for i in range(len(nums))]
        for n in range(2,len(nums)):
            for i in range(0,len(nums)-n):
                j=i+n
                m=0
                for k in range(i+1, j):
                    left=dp[i][k]
                    right=dp[k][j]
                    m=max(m,left+right+nums[i]*nums[j]*nums[k])
                dp[i][j]=m
        return dp[0][len(nums)-1]
        
# @lc code=end



#
# @lcpr case=start
# [3,1,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,5]\n
# @lcpr case=end

#

