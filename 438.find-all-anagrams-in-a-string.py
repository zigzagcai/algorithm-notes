#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans=[]
        for right, c in enumerate(s):
            cnt_s[c]+=1
            left=right-len(p)+1
            if left<0:
                continue
            if cnt_s==cnt_p:
                ans.append(left)
            left_val=s[left]
            cnt_s[left_val]-=1
            if cnt_s[left_val] == 0:
                del cnt_s[left_val]
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

