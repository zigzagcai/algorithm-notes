#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i: int, target_left: int) -> None:
            if target_left==0:
                ans.append(path[:])
                return
            
            if i==len(candidates) or target_left<0:
                return
            
            # not choose
            dfs(i+1, target_left)
            
            # choose
            path.append(candidates[i])
            dfs(i, target_left-candidates[i])
            path.pop()
        
        dfs(0,target)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

