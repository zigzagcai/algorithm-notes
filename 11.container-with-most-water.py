#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        while(left<right):
            ans = max(ans, (right-left)*min(height[left], height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
        
        
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

