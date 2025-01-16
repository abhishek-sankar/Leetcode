class RandomizedSet:

    def __init__(self):
        self.randomizedSet = []
        self.indexList = {}

    def search(self, val):
        return val in self.indexList

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False

        self.randomizedSet.append(val)
        self.indexList[val] = len(self.randomizedSet) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False

        idx = self.indexList[val]
        self.randomizedSet[idx] = self.randomizedSet[-1]
        self.indexList[self.randomizedSet[-1]] = idx
        self.randomizedSet.pop()
        del self.indexList[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomizedSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
