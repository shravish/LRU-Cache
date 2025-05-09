from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move key to end to show it's recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update key and mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove least recently used (first key)
            self.cache.popitem(last=False)
# capacity 2
'''
lru = LRUCache(2)
lru.put(1, 100)      
# Cache: {1: 100}
lru.put(2, 200)       
# Cache: {1: 100, 2: 200}
print(lru.get(1))     
# Returns 100, Cache becomes {2: 200, 1: 100}
lru.put(3, 300)       
# Evicts key 2, Cache: {1: 100, 3: 300}
print(lru.get(2))     
# Returns -1 (key 2 was evicted)
'''
# capacity 2
lru = LRUCache(2)
lru.put(1, 1)       
# Cache: {1:1}
lru.put(2, 2)       
# Cache: {1:1, 2:2}
print(lru.get(1))   
# Returns 1, Cache: {2:2, 1:1}
lru.put(3, 3)       
# Cache is full, removes key 2 → Cache: {1:1, 3:3}
print(lru.get(2))   
# Returns -1 (not found)
lru.put(4, 4)       
# Removes key 1 → Cache: {3:3, 4:4}
print(lru.get(1))   
# Returns -1
print(lru.get(3))   
# Returns 3
print(lru.get(4))   
# Returns 4

#capacity 3
lru = LRUCache(3)
lru.put(10, 'A')     
# Cache: {10: 'A'}
lru.put(20, 'B')     
# Cache: {10: 'A', 20: 'B'}
lru.put(30, 'C')    
# Cache: {10: 'A', 20: 'B', 30: 'C'}
print(lru.get(10))   
# Returns 'A' → moves 10 to end → {20, 30, 10}
lru.put(40, 'D')     
# Cache full, removes 20 → {30, 10, 40}
print(lru.get(20))   
# Returns -1 (20 was evicted)
print(lru.get(30))   
# Returns 'C'
lru.put(50, 'E')     
# Removes 10 → {40, 30, 50}
print(lru.get(10))   
# Returns -1
print(lru.get(40))   
# Returns 'D'
print(lru.get(50))   
# Returns 'E'
