class MapSum:

    def __init__(self):
        self.d = dict()

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        matched_keys = filter(lambda key: key.startswith(prefix), self.d.keys())
        _sum = 0
        for k in matched_keys:
            _sum += self.d[k]
        return _sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)