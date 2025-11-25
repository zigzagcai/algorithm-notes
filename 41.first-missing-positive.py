#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        hash_size = n+1
        
        for i in range(n):
            if nums[i]<=0 or nums[i]>=hash_size:
                nums[i]=0
        
        for i in range(n):
            if nums[i]%hash_size!=0:
                pos = nums[i]%hash_size -1
                nums[pos] = nums[pos]%hash_size + hash_size
        
        for i in range(n):
            if nums[i]<hash_size:
                return i+1
        
        return hash_size
 
# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

