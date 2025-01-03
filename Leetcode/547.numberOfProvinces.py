class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected = [False] * len(isConnected)
        n = len(isConnected)

        def dfs(i):
            for neighbour in range(n):
                if connected[neighbour] == False and isConnected[i][neighbour] == 1:
                    connected[neighbour] = True
                    dfs(neighbour)

        provinces = 0
        for i in range(len(isConnected)):
            if not connected[i]:
                provinces += 1
                dfs(i)

        return provinces
