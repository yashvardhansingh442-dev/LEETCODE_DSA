from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key)
        if not arr:
            return ""
        # find the first index whose timestamp > the query timestamp
        i = bisect_right(arr, (timestamp, chr(127)))
        return arr[i - 1][1] if i else ""