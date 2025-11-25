#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [0]*n
        col = [False]*n
        diag1 = [False]*(2*n-1)
        diag2 = [False]*(2*n-1)
        def dfs(r: int)->None:
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-c-1) for c in queens])
                return
            for c, ok in enumerate(col):
                if not ok and not diag1[r+c] and not diag2[r-c]:
                    queens[r] = c
                    col[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r+1)
                    col[c] = diag1[r+c] = diag2[r-c] = False
        dfs(0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

