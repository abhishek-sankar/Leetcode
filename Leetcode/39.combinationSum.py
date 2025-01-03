class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combination_sum_helper(candidates, remaining, current, current_index, res):
            
            for i in range(current_index, len(candidates)):
                if candidates[i] < remaining:
                    _current = current.copy()
                    _current.append(candidates[i])
                    # print(_current, candidates[i], " is less than", remaining)
                    combination_sum_helper(candidates, remaining - candidates[i], _current, max(current_index, i), res)
                elif candidates[i] == remaining:
                    _current = current.copy()
                    _current.append(candidates[i])
                    # print("Adding", _current)
                    res.append(_current)
        
        
        res = []
        candidates.sort()
        combination_sum_helper(candidates, target, [], 0, res)

        return res

