#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        @cache
        def dfs(i:int, j:int)->int:
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i]==word2[j]:
                return dfs(i-1,j-1)
            else:
                return min(dfs(i-1,j-1),dfs(i-1,j),dfs(i,j-1))+1
        return dfs(n-1,m-1)
        
# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

