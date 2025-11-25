#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i: int)->None:
            if i == n:
                ans.append(path[:])
                return
            
            # NO select
            dfs(i+1)
            
            # select
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
                
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

