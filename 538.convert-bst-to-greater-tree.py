#
# @lc app=leetcode.cn id=538 lang=python3
# @lcpr version=30204
#
# [538] 把二叉搜索树转换为累加树
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
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s=0
        def dfs(node:TreeNode)->None:
            if node is None:
                return
            dfs(node.right)
            nonlocal s
            s+=node.val
            node.val=s
            dfs(node.left)
        dfs(root)
        return root
        
# @lc code=end



#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4,1]\n
# @lcpr case=end

#

