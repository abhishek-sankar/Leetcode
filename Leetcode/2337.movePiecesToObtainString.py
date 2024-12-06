class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left_indices_start = [idx for idx, ele in enumerate(start) if ele == "L"]
        left_indices_target = [idx for idx, ele in enumerate(target) if ele == "L"]
        
        right_indices_start = [idx for idx, ele in enumerate(start) if ele == "R"]
        right_indices_target = [idx for idx, ele in enumerate(target) if ele == "R"]

        if len(left_indices_start) != len(left_indices_target):
            return False
        
        if len(right_indices_start) != len(right_indices_target):
            return False
        
        for i in range(len(left_indices_start)):
            if left_indices_start[i] < left_indices_target[i]:
                return False

        for i in range(len(right_indices_start)):
            if right_indices_start[i] > right_indices_target[i]:
                return False

        return "".join([s for s in start if s != "_"]) == "".join([s for s in target if s != "_"]) and len(start) == len(target)
