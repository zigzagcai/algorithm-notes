#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n - 1
        while left<=right:
            mid = (left+right)//2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

