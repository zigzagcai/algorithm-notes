#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=30204
#
# [85] 最大矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxRectangle(nums: List[int])->int:
            nums = [0] + nums + [0]
            st=[]
            ans=0
            for right,num in enumerate(nums):
                while st and nums[st[-1]]>num:
                    idx=st.pop()
                    ans=max(ans, nums[idx]*(right-st[-1]-1))
                st.append(right)
            return ans
        
        n=len(matrix[0])
        heights=[0]*n
        ans=0
        for row in matrix:
            for j,c in enumerate(row):
                if c=='0':
                    heights[j]=0
                else:
                    heights[j]+=1
            ans=max(ans,maxRectangle(heights))
        return ans
                
        
# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

#

