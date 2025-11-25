#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
MAPPING = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        ans=[]
        path=['']*n
        def dfs(i:int)->None:
            if i==n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i]=c
                dfs(i+1)
        dfs(0)
        return ans
            
        
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

