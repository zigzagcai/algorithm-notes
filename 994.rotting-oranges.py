#
# @lc app=leetcode.cn id=994 lang=python3
# @lcpr version=30204
#
# [994] 腐烂的橘子
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        fresh=0
        q=[]
        ans=0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x==1:
                    fresh+=1
                if x==2:
                    q.append((i,j))
        while q and fresh:
            ans+=1
            tmp=q
            q=[]
            for x,y in tmp:
                for i,j in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        fresh-=1
                        grid[i][j]=2
                        q.append((i,j))
        return -1 if fresh else ans
        
# @lc code=end



#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#

