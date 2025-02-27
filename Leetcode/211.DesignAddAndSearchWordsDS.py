class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def search_helper(root, str):
            if str is None or str == "":
                return root.isEnd
            if str[0] in root.children:
                return search_helper(root.children[str[0]], str[1:])
            elif str[0] == ".":
                flag = False
                for child in root.children:
                    if(search_helper(root.children[child], str[1:])):
                        flag = True
                return flag
            else:
                return False
        return search_helper(self.root, word)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)