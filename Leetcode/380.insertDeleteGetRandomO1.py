class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        self.randomizedSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_element = random.sample(sorted(self.randomizedSet), 1)[0]
        return random_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
