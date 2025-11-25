#
# @lc app=leetcode.cn id=494 lang=python3
# @lcpr version=30204
#
# [494] 目标和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s=sum(nums)-abs(target)
        if s<0 or s%2:
            return 0
        
        @cache
        def dfs(i:int, c:int)->int:
            if i<0:
                return 1 if c==0 else 0
            if c<nums[i]:
                return dfs(i-1,c)
            else:
                return dfs(i-1,c)+dfs(i-1,c-nums[i])
            
        m=s//2
        return dfs(len(nums)-1, m)
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

