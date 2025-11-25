#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import inf


class MinStack:

    def __init__(self):
        self.st=[(0,inf)]   # (val,minval)
        
    def push(self, val: int) -> None:
        self.st.append((val,min(self.st[-1][1],val)))
        
    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]
        
    def getMin(self) -> int:
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

