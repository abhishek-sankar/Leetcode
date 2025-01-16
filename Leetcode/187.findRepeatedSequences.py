class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)
        dna = list(s)
        for i in range(len(s) - 9):
            current = "".join(dna[i : i + 10])
            sequences[current] = sequences.get(current, 0) + 1
        return [seq for seq, count in sequences.items() if count > 1]
