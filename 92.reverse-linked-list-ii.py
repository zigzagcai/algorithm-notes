#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = p0 = ListNode(next=head)
        for _ in range(left-1):
            p0=p0.next
        cur = p0.next
        prev = None
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        p0.next.next = cur
        p0.next = prev
        return dummy.next
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

