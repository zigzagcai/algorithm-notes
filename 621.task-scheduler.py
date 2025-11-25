#
# @lc app=leetcode.cn id=621 lang=python3
# @lcpr version=30204
#
# [621] 任务调度器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_count = list(Counter(tasks).values())
        maxFreq = max(dict_count)
        eleMaxFreq = dict_count.count(maxFreq)
        return max((maxFreq-1)*(n+1)+eleMaxFreq, len(tasks))
        
# @lc code=end



#
# @lcpr case=start
# ["A","A","A","B","B","B"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["A","C","A","B","D","B"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["A","A","A","B","B","B"]\n3\n
# @lcpr case=end

#

