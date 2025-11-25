#
# @lc app=leetcode.cn id=448 lang=python3
# @lcpr version=30204
#
# [448] 找到所有数组中消失的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        return [idx+1 for idx, num in enumerate(nums) if num>0]
        
# @lc code=end



#
# @lcpr case=start
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

