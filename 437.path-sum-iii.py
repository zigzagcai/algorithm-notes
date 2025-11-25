#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III
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
from typing import Counter


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        dic = Counter()
        dic[0]=1
        def dfs(root, s):
            if root==None:
                return
            s+=root.val
            nonlocal ans
            ans+=dic[s-targetSum]
            dic[s]+=1
            dfs(root.left, s)
            dfs(root.right, s)
            dic[s]-=1
        dfs(root,0)
        return ans
            
        
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

