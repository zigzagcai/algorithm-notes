#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import inf


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxlen=-inf
        ans=''
        f=[[True]*n for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            f[i][i]=True
            for j in range(i,n):
                f[i][j]=s[i]==s[j] and f[i+1][j-1]
                if f[i][j] and j-i+1>maxlen:
                    maxlen=j-i+1
                    ans=s[i:j+1]
        return ans
        
        
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

