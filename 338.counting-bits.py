#
# @lc app=leetcode.cn id=338 lang=python3
# @lcpr version=30204
#
# [338] 比特位计数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(1, n+1):
            ans[i]=ans[i>>1]+(i&1)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

