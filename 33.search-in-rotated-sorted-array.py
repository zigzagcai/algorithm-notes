#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a,b]
        def find_min(nums: List[int]) -> int:
            left, right = 0, len(nums) - 2
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<nums[-1]:
                    right=mid-1
                else:
                    left=mid+1
            return left

        # [a,b]
        def lower_bound(nums, left, right, target):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left if nums[left]==target else -1
        
        i=find_min(nums)
        if target>nums[-1]:
            return lower_bound(nums, 0, i-1, target)
        else:
            return lower_bound(nums, i, len(nums)-1, target)
        
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

