#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = ['']*2*n
        def dfs(l, r):
            if r==n:
                ans.append(''.join(s))
            if l<n:
                s[l+r] = '('
                dfs(l+1, r)
            if r<l:
                s[l+r] = ')'
                dfs(l, r+1)
        dfs(0,0)
        return ans

    
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

