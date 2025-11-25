#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.


from heapq import heapify, heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        h = [(head.val,i) for i,head in enumerate(lists) if head]
        heapify(h)
        while h:
            val, i = heappop(h)
            node = ListNode(val)
            cur.next = node
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(h, (lists[i].val, i))
        return dummy.next
                
            
        
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

