#
# @lc app=leetcode.cn id=581 lang=python3
# @lcpr version=30204
#
# [581] 最短无序连续子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        right, left = 0,n-1
        maxPre = nums[0]
        minpost = nums[-1]
        for i in range(n):
            if nums[i]>=maxPre:
                maxPre=nums[i]
            else:
                right=i
            if nums[n-1-i]<=minpost:
                minpost=nums[n-1-i]
            else:
                left=n-1-i
        return 0 if right==0 else right-left+1
        
# @lc code=end



#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

