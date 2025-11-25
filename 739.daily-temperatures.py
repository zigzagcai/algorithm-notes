#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0]*n
        for i in range(n-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

