#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30204
#
# [96] 不同的二叉搜索树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1,1]
        if n<=1:
            return dp[n]
        for m in range(2,n+1):
            count=0
            for j in range(m):
                count+=dp[j]*dp[m-j-1]
            dp.append(count)
        return dp[n]
        
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

