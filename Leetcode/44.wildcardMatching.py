def isMatch(s: str, p: str) -> bool:
    flag = [False]

    def dfs(si, pi):
        print(si, pi)
        if si >= len(s) and pi >= len(p):
            flag[0] = True
            return
        if pi >= len(p):
            return

        if s[si] == p[pi]:
            dfs(si + 1, pi + 1)
        elif p[pi] == "?":
            dfs(si + 1, pi + 1)
        elif p[pi] == "*":
            if pi + 1 < len(p) and si + 1 < len(s):
                if s[si + 1] == p[pi + 1]:
                    dfs(si + 1, pi + 1)
                else:
                    dfs(si + 1, pi)
            elif pi == len(p) - 1:
                flag[0] = True
                return
            else:
                key = True
                for j in range(pi, len(p)):
                    if p[j] != "*":
                        key = False
                if key:
                    flag[0] = True
                return

    dfs(0, 0)
    return flag


print(isMatch("aa", "*"))
