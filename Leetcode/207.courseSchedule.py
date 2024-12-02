class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child] -=1
                if indegree[child] == 0:
                    q.append(child)
        
        return len(ans) == numCourses