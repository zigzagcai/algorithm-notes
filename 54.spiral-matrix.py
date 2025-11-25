#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = (0,1), (1,0), (0, -1), (-1, 0)
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        i = j = 0
        di = 0
        for _ in range(row*col):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i+dirs[di][0], j+dirs[di][1]
            if x<0 or x>=row or y<0 or y>=col or matrix[x][y] is None:
                di = (di + 1) % 4
            i += dirs[di][0]
            j += dirs[di][1]
        return ans
            
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

