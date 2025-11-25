#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        mx=0
        cur=0
        for i,num in enumerate(nums[:-1]):
            mx = max(mx, i+num)
            if i==cur:
                cur=mx
                ans+=1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

