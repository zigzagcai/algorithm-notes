#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        permute_ids = [0]*n
        visited = [False]*n
        def dfs(item: int) -> None:
            if item==n:
                ans.append([nums[i] for i in permute_ids])
            for idx, ok in enumerate(visited):
                if not ok:
                    permute_ids[item]=idx
                    visited[idx]=True
                    dfs(item+1)
                    visited[idx]=False
        dfs(0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

