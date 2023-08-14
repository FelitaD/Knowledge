Organises data to quickly look up a value with a key.

Pros:
- Fast lookups average O(1)
- Flexible keys when hashable

Cons:
- Slow worst-case lookup with O(n) -> if all keys caused hash collision
- Unordered
- Single-directional lookups
- Not cache-friendly

**Hash collisions**

Hash tables built on arrays that have a fixed size.
How to resolve hash collisions? With linked lists
![[Pasted image 20230622003926.png|400]]