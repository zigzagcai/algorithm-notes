#
# @lc app=leetcode.cn id=309 lang=python3
# @lcpr version=30204
#
# [309] 买卖股票的最佳时机含冷冻期
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i:int, hold:bool)->int:
            if i<0:
                if hold:
                    return -inf
                else:
                    return 0
            if hold:
                return max(dfs(i-1,True),dfs(i-2,False)-prices[i])
            else:
                return max(dfs(i-1,False),dfs(i-1,True)+prices[i])
            
        return dfs(n-1,False)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

