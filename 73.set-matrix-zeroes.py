#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]
        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0
        
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

