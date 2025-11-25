#
# @lc app=leetcode.cn id=763 lang=python3
# @lcpr version=30204
#
# [763] 划分字母区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last = {}
        # for i,c in enumerate(s):
        #     last[c] = i
        last = {c:i for i,c in enumerate(s)}
        start=end=0
        ans=[]
        for i,c in enumerate(s):
            end=max(end,last[c])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "ababcbacadefegdehijhklij"\n
# @lcpr case=end

# @lcpr case=start
# "eccbbbbdec"\n
# @lcpr case=end

#

