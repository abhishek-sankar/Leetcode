class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        return trie.searchAndDFS(searchWord)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def searchAndDFS(self, word):
        res = []
        node = self.root
        current = []
        for idx, ch in enumerate(word):
            word_results = []
            if ch not in node.children:
                res.extend([[] for _ in range(len(word) - idx)])
                return res
            current.append(ch)
            node = node.children[ch]
            dfsNode = node
            self.dfs(dfsNode, current, word_results)
            res.append(word_results)
        return res

    def dfs(self, node, current, word_results):
        if node.isEnd:
            word_results.append("".join(current))
        if len(word_results) < 3:
            for ch in sorted(node.children):
                if len(word_results) < 3:
                    current.append(ch)
                    self.dfs(node.children[ch], current, word_results)
                    current.pop()
        else:
            return


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
