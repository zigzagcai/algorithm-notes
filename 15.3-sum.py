#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if (not nums) or n<3:
            return ans
        nums.sort()
        for i in range(n-2):
            if nums[i]>0:
                return ans
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L = i+1
            R = n-1
            while(L<R):
                if nums[i]+nums[L]+nums[R]==0:
                    ans.append([nums[i], nums[L], nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L+=1
                    while(L<R and nums[R]==nums[R-1]):
                        R-=1
                    L+=1
                    R-=1
                elif nums[i]+nums[L]+nums[R]<0:
                    L+=1
                else:
                    R-=1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

