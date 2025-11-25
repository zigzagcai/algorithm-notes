#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import inf, isqrt

@cache
def dfs(i:int, j:int)->int:
    if i==0:
        return inf if j else 0
    if j<i*i:
        return dfs(i-1,j)
    else:
        return min(dfs(i-1,j),dfs(i,j-i*i)+1)

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n),n)
        
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

