#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        cnt_s = Counter()
        right_ptr = len(s)
        left_ptr = -1
        left = 0
        for right, c in enumerate(s):
            cnt_s[c]+=1
            while cnt_s>=cnt_t:
                if right - left < right_ptr - left_ptr:
                    right_ptr, left_ptr = right, left
                cnt_s[s[left]]-=1
                left+=1
        return '' if left_ptr==-1 else s[left_ptr:right_ptr+1]

# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

