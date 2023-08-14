Stores things in order but not necessarily in contiguous blocks of memory.

![[Pasted image 20230616154950.png]]

2 types:
- Singly Linked Lists
- Doubly Linked Lists

## Implementation

No built-in linked list in Python. Can make a user-defined linked list:
```python
class LinkedList:
```

Implement other data structures :
- Stacks
- Queues 
- Graphs

## Operations & Complexity

Search: need to traverse all the nodes so O(n)
Insertion: O(1)
Deletion: O(1)

Faster insertions and deletions than arrays, but slower lookups (walk down the whole list).