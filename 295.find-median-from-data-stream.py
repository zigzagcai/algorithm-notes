#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.left = [] # maxheap
        self.right = [] # minheap
    
    def addNum(self, num: int):
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, num))
        else:
            heappush(self.right, -heappushpop(self.left, -num))
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



