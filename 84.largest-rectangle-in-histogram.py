#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, heights[tmp] * ((i-1)-(stack[-1]+1)+1))
            stack.append(i)
        return res
        
# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

 