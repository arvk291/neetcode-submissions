import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Use defaultdict to automatically create empty lists for new keys
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append tuple to preserve history; do not overwrite
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Edge Case 1: Key does not exist
        if key not in self.timeMap:
            return ""
        
        entries = self.timeMap[key]
        
        # Binary Search: Find the rightmost position where (timestamp, high_char) could go
        # We use chr(127) ('~') as a sentinel because it's lexicographically larger 
        # than any standard alphanumeric character, ensuring we find the correct 
        # insertion point even if timestamps match exactly.
        idx = bisect.bisect_right(entries, (timestamp, chr(127)))
        
        # Edge Case 2: All stored timestamps are greater than the query timestamp
        # idx will be 0, meaning no valid element exists to the left
        if idx == 0:
            return ""
        
        # The element at idx - 1 is the largest timestamp <= query timestamp
        return entries[idx - 1][1]   