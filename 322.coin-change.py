#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


from functools import cache
from math import inf


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
        
    #     @cache
    #     def dfs(i: int, c: int) -> int:
    #         if i<0:
    #             return 0 if c==0 else inf
    #         if c<coins[i]:
    #             return dfs(i-1, c)
    #         return min(dfs(i-1,c), dfs(i,c-coins[i])+1)
        
    #     ans = dfs(len(coins)-1, amount)
    #     return ans if ans<inf else -1
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf]*(amount+1) for _ in range(n+1)]
        f[0][0] = 0
        for i,x in enumerate(coins):
            for c in range(amount+1):
                if c<x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = min(f[i][c], f[i+1][c-x]+1)
        ans = f[n][amount]
        return ans if ans<inf else -1
        
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

