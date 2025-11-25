#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        
        color = [0]*numCourses
        def dfs(u: int) -> bool:
            color[u] = 1
            for v in adj[u]:
                if color[v]==1:
                    return True
                if color[v]==0:
                    if dfs(v):
                        return True
                if color[v]==2:
                    pass
            color[u] = 2
            return False
            
        
        for i in range(numCourses):
            if color[i]==0:
                if dfs(i):
                    return False
        return True
    
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     adj = [[] for _ in range(numCourses)]
    #     indegree = [0]*numCourses
    #     for cur, pre in prerequisites:
    #         adj[pre].append(cur)
    #         indegree[cur]+=1
        
    #     queue = deque()
    #     count = numCourses
    #     for i in range(numCourses):
    #         if indegree[i]==0:
    #             queue.append(i)
    #     while(queue):
    #         pre = queue.popleft()
    #         count-=1
    #         for cur in adj[pre]:
    #             indegree[cur]-=1
    #             if indegree[cur]==0:
    #                 queue.append(cur)
    #     return count==0
                    
        
        
        
            
        
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

