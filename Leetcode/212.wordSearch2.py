class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = Trie()
        for word in words:
            wordTrie.insert(word)
        
        visiting = set()
        words = set()
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return []

        def dfs(r, c, cur, word):
            if cur.isEnd:
                words.add(word)
            visiting.add((r, c))
            directions = [(-1,0), (1,0), (0, -1), (0,1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nc < n and 0 <= nr < m and (nr, nc) not in visiting and board[nr][nc] in cur.children:
                    dfs(nr, nc, cur.children[board[nr][nc]], word + board[nr][nc])
            visiting.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = wordTrie.root
                if board[r][c] in cur.children:
                    dfs(r, c, cur.children[board[r][c]], board[r][c])
        
        return [word for word in words]

class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isEnd = True
    
    def search(self, word):
        cur = self.root
        for letter in word:
            if not letter in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isEnd