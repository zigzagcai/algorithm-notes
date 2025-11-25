#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30204
#
# [1143] 最长公共子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        @cache
        def dfs(i:int, j:int)->int:
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return dfs(i-1,j-1)+1
            else:
                return max(dfs(i-1,j),dfs(i,j-1))
        return dfs(n-1,m-1)
        
# @lc code=end



#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

