class TimeMap:

    def __init__(self):
        self._hash_set = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._hash_set:
            self._hash_set[key] = []
        
        self._hash_set[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._hash_set:
            return ""

        get_list = self._hash_set[key]
        l, r = 0, len(get_list) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if get_list[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid
        if get_list[l][1] > timestamp:
            return ""
        return get_list[l][0]