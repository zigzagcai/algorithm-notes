#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     pre = [1]*n
    #     # pre[i]=nums[0]*...*nums[i-1], i>=1, i<n
    #     for i in range(1, n):
    #         pre[i] = pre[i-1]*nums[i-1]
    #     # suf[i]=nums[i+1]*...*nums[n-1], i<=n-2, i>=0
    #     suf = [1]*n
    #     for i in range(n-2, -1, -1):
    #         suf[i] = suf[i+1]*nums[i+1]
    #     return [p*s for p,s in zip(pre, suf)]
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1]*n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1]*nums[i+1]
        pre = 1
        for i, x in enumerate(nums):
            suf[i] *= pre
            pre *= x
        return suf
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

