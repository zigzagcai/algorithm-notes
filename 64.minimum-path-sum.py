#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                elif j==0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i==0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
        return grid[-1][-1]
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

