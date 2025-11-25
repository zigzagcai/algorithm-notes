#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left=-inf,right=inf):
            if node is None:
                return True
            val=node.val
            if not (left < val < right):
                return False
            return dfs(node.left,left,val) and dfs(node.right,val,right)
        return dfs(root)
        
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

