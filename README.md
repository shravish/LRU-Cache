# LRU-Cache
The LRU Cache question is about designing a system that remembers the most recently used items and automatically forgets the least recently used ones when it gets full.

Here’s the setup:

You're given a fixed capacity for the cache—say, 2.

You need to support two actions:
get(key): Return the value for a key if it exists, otherwise return -1.
put(key, value): Insert or update the value for the key. If adding this key would go over capacity, you remove the least recently used key.

So basically, every time a key is accessed or added, it becomes the “most recently used.” And if the cache is full, you kick out the “least recently used” key.

Let’s say the capacity is 2 and you do:

put(1, 1) → cache: {1: 1}

put(2, 2) → cache: {1: 1, 2: 2}

get(1) → returns 1 and moves key 1 to “most recently used” → cache: {2: 2, 1: 1}

put(3, 3) → key 2 is least recently used, so it's removed → cache: {1: 1, 3: 3}

To build an efficient LRU cache, we want both get and put operations to work in constant time—O(1).

The trick is to combine two data structures:
A dictionary (or hashmap) for fast key lookups, and a doubly linked list to track usage order.

But Python makes this easier! You can just use collections.OrderedDict, which keeps the order of insertion and lets you move keys to the end when they’re used.

Here's how it works:

Use the keys of the OrderedDict as your cache keys.

When a key is accessed or updated, move it to the end to mark it as most recently used.

When adding a new key and you're over capacity, pop the first key (which is the least recently used).
