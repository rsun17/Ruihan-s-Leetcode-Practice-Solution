# 0705 Design HashSet - Easy
# https://leetcode.com/problems/design-hashset
# https://leetcode.com/problems/design-hashset
# Tags: Array | Hash Table | Linked List | Design | Hash Function

class MyHashSet:
    def __init__(self):
        self._size = 769
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key: int) -> int:
        return key % self._size

    def add(self, key: int) -> None:
        i = self._hash(key)
        bucket = self._buckets[i]
        for v in bucket:
            if v == key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        i = self._hash(key)
        bucket = self._buckets[i]
        for idx, v in enumerate(bucket):
            if v == key:
                bucket[idx] = bucket[-1]
                bucket.pop()
                return

    def contains(self, key: int) -> bool:
        i = self._hash(key)
        for v in self._buckets[i]:
            if v == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)