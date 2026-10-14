class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        self.cache_dict.move_to_end(key)
        return self.cache_dict[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_dict.move_to_end(key)
        self.cache_dict[key] = value

        if len(self.cache_dict) > self.capacity:
            self.cache_dict.popitem(last=False)