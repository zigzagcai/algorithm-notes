#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]
        for idx,num in enumerate(nums):
            # left: idx-k+1, right:idx
            while q and q[0]<idx-k+1:
                q.popleft()
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(idx)
            if idx-k+1>=0:
                ans.append(nums[q[0]])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

