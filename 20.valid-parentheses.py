#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            elif not stack or stack.pop()!=map[c]:
                return False
        return not stack
                
        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

