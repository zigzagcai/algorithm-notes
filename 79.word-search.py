#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def dfs(i: int, j:int, k:int)->bool:
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            board[i][j]=''
            for x,y in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=x<n and 0<=y<m and dfs(x,y,k+1):
                    return True
            board[i][j]=word[k]
            return False
        return any(dfs(i,j,0) for i in range(n) for j in range(m))
        
        
# @lc code=end



#
# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCB"\n
# @lcpr case=end

#

