#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                c[i][j] = c[i-1][j-1] + c[i-1][j]
        return c
        
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

