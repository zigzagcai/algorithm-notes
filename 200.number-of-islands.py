#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def dfs(i:int, j:int)->None:
            grid[i][j]='0'
            for i1,j1 in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=i1<row and 0<=j1<col and grid[i1][j1]=='1':
                    dfs(i1,j1)
            return
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count
                
        
# @lc code=end



#
# @lcpr case=start
# [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]\n
# @lcpr case=end

# @lcpr case=start
# [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]\n
# @lcpr case=end

#

