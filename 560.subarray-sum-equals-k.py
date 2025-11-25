#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]*(n+1)
        for idx, num in enumerate(nums):
            prefix_sum[idx+1] = prefix_sum[idx]+num
        cnt = defaultdict(int)
        ans = 0
        for sj in prefix_sum:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans
                
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

