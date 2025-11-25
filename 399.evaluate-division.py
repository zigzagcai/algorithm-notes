#
# @lc app=leetcode.cn id=399 lang=python3
# @lcpr version=30204
#
# [399] 除法求值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(list)
        for (n1,n2), v in zip(equations,values):
            g[n1].append([n2,v])
            g[n2].append([n1,1/v])
        lst=[]
        
        def dfs(cur,end,tot)->bool:
            if cur==end:
                nonlocal res
                res=tot
                return True
            vis.add(cur)
            for nxt,v in g[cur]:
                if nxt not in vis:
                    # prune
                    if dfs(nxt,end,tot*v):
                        return True
            return False
        
        for start,end in queries:
            vis=set()
            res=-1.0
            if start in g and end in g:
                dfs(start,end,1)
            lst.append(res)
        return lst
        
# @lc code=end



#
# @lcpr case=start
# [["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["b","c"],["bc","cd"]]\n[1.5,2.5,5.0]\n[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"]]\n[0.5]\n[["a","b"],["b","a"],["a","c"],["x","y"]]\n
# @lcpr case=end

#

