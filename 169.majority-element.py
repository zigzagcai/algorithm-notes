#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30204
#
# [169] 多数元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        hp = 0
        for num in nums:
            if hp==0:
                ans, hp = num, 1
            else:
                hp+=1 if num==ans else -1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

