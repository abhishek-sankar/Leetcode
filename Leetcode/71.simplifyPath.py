class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        s = deque()
        for dir in dirs:
            if dir == ".":
                continue
            elif dir == "..":
                if s:
                    s.pop()
            else:
                if dir:
                    s.append(dir)
        res = []
        while s:
            dir = s.popleft()
            if dir:
                res.append(dir)
        return "/" + "/".join(res)
