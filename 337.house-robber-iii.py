#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30204
#
# [337] 打家劫舍 III
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
from typing import Optional, Tuple


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode])->Tuple[int,int]:
            if root is None:
                return 0,0
            l_rob, l_not_rob = dfs(root.left)
            r_rob, r_not_rob = dfs(root.right)
            rob = l_not_rob+r_not_rob+root.val
            not_rob = max(l_rob,l_not_rob)+max(r_rob,r_not_rob)
            return rob, not_rob
        return max(dfs(root))
        
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#

