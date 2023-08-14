Stores things in order in the memory.
Has quick lookups by index.
Need to specify the size ahead of time.

![[Pasted image 20220914000811.png|300]]

## Implementation

```python
import array

a = array.array('i', [1, 2, 3, 4])
a/3
```
array() module is more efficient for large amounts of data and math operations than list
```python
l = [1, 2, 3, 4]
```

## Operations & Complexity

Access (lookup value with index): O(1)
Search: O(n)
Insertion: O(n)
Deletion: O(n)

Insertion and deletion need to reallocate each block one by one to reform a contiguous memory block. Stacks, queues and linked lists don't have this problem.

****
https://www.interviewcake.com/concept/python3/array?course=fc1&section=array-and-string-manipulation
*****

[[Strings]]
[[Matrix]]
[[Struct]]