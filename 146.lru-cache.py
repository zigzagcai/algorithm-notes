#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.dummy = Node(-1, -1)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
    
    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node:
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.map) == self.capacity:
                remove_key = self.dummy.next.key
                self._remove(self.dummy.next)
                del self.map[remove_key]
            new_node = Node(key, value)
            self.map[key] = new_node
            self._add_to_tail(new_node)
               
    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_tail(self, node) -> None:
        tail = self.dummy.prev
        tail.next = node
        node.prev = tail
        node.next = self.dummy
        self.dummy.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



