class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq_ctr = [0] * 26
        for word in words2:
            counts = Counter(word)
            for ch, count in counts.items():
                max_freq_ctr[ord(ch) - ord('a')] = max(max_freq_ctr[ord(ch) - ord('a')], count)
        


        def checkIfSubset(source: List[int], target: str) -> bool:
            target_counter = Counter(target)
            for i in range(26):
                if source[i] > target_counter[chr(ord('a') + i)]:
                    return False
            
            return True
        
        return [word for word in words1 if checkIfSubset(max_freq_ctr, word)]
            
        