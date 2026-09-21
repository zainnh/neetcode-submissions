class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
        self.cache.move_to_end(key)
        return self.cache[key]

    # ok i guess in Python, move_to_end() is a specialized method belonging to the collections.OrderedDict class. It allows you to shift an existing key-value pair to either the far right (end) or far left (beginning) of the dictionary in efficient O(1) time complexity. Just some random bs bro. 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) 

# LRU = Least Retarded User
