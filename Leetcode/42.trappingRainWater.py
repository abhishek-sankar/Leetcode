class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        ldp = [0] * len(height)
        rdp = [0] * len(height)

        l_max = height[0]
        r_max = height[-1]
        for i in range(1, len(height)):
            ldp[i] = l_max
            l_max = max(height[i], l_max)

        for i in range(len(height) - 2, -1, -1):
            rdp[i] = r_max
            r_max = max(height[i], r_max)

        water = 0
        for i in range(1, len(height) - 1):
            water += max(min(ldp[i], rdp[i]) - height[i], 0)

        return water
