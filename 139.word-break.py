#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxlen = max(map(len, wordDict))
        st = set(wordDict)
        n = len(s)
        
        @cache
        def dfs(i) -> bool:
            if i==0:
                return True
            for j in range(i-1, max(i-maxlen-1, -1), -1):
                if s[j:i] in st and dfs(j):
                    return True
            return False
        
        return dfs(n)
        
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

