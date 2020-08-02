class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.obj = set()

    def add(self, key: int) -> None:
        self.obj.add(key)
    
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.obj.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.obj and (key in self.obj):
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
