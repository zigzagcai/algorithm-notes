#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        k = 0
        for c in s:
            if c.isalpha():
                res+=c
            elif c.isdigit():
                k=10*k+int(c)
            elif c=='[':
                stack.append((res,k))
                res=''
                k=0
            else:
                pre_res, pre_k = stack.pop()
                res=pre_res+res*pre_k
        return res
        
# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#

