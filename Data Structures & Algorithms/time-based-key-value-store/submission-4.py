class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        timestamp_mapping = self.time_map[key]
        timestamp_mapping.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamp_mapping = self.time_map.get(key, [])
        low = 0
        high = len(timestamp_mapping) - 1
        while low <= high:
            mid = ((high - low) // 2) + low
            if timestamp_mapping[mid][0] <= timestamp:
                if mid < high:
                    if timestamp < timestamp_mapping[mid + 1][0]:
                        return timestamp_mapping[mid][1]
                    else:
                        low = mid + 1  
                else:
                    return timestamp_mapping[mid][1]
            else:
                high = mid - 1
        return ""
        
