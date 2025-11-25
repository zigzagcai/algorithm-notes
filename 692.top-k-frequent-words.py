#
# @lc app=leetcode.cn id=692 lang=python3
# @lcpr version=30204
#
# [692] 前K个高频单词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        import heapq
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
# @lc code=end



#
# @lcpr case=start
# ["i", "love", "leetcode", "i", "love", "coding"]\n2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

