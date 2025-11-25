#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i,target):
            if i<0:
                return target==0
            if target<nums[i]:
                return dfs(i-1,target)
            else:
                return dfs(i-1,target-nums[i]) or dfs(i-1,target)
        s=sum(nums)
        return s%2==0 and dfs(len(nums)-1,s//2)
        
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

