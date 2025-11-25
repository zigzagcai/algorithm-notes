#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack_size=0
        for x in nums:
            if x:
                nums[stack_size]=x
                stack_size+=1
        for i in range(stack_size, len(nums)):
            nums[i]=0
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

