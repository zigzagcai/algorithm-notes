#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        ans=0
        for i, c in enumerate(s):
            if c=='(':
                st.append(i)
            elif len(st)>1:
                st.pop()
                ans=max(ans, i-st[-1])
            else:
                st[0]=i
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#

