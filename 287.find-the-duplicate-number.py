#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#

