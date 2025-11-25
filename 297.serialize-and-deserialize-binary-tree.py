#
# @lc app=leetcode.cn id=297 lang=python3
# @lcpr version=30204
#
# [297] 二叉树的序列化与反序列化
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        queue = deque()
        queue.append(root)
        res=[]
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '['+','.join(res)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='[]':
            return
        vals, i = data[1:-1].split(','), 1
        root=TreeNode(int(vals[0]))
        queue=deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i]!='null':
                node.left=TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            if vals[i] != "null":
                node.right=TreeNode(int(vals[i]))
                queue.append(node.right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,null,4,5]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

