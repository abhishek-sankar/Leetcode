class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devvowel(word):
            return "".join("*" if c in "aeiou" else c for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vowel = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vowel.setdefault(devvowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devvowel(queryL)
            if queryLV in words_vowel:
                return words_vowel[queryLV]

            return ""

        return list(map(solve, queries))
        # return [solve(query) for query in queries]
