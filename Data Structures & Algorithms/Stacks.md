
LIFO: Like a stack of dirty plates: can only put and remove one at the top.

## Implementation

- list
- **collections.deque**
- queue.LifoQueue

```python
plates = []

plates.append('plate1')
plates.append('plate2')
plates.append('plate3')

plates.pop()
>>> 'plate3'
```

```python
from collections import deque

plates = deque()

plates.append('plate1')
plates.append('plate2')
plates.append('plate3')

plates.pop()
>>> 'plate3'
```

Difference between list and double-ended queue with memory reallocation.

Thread-safe:
- List -> no 
- deque (double-ended queue) -> no except pop() and append()
- LifoQueue -> yes

## Operations & Complexity

Search: need to traverse all the nodes so O(n)
Insertion: O(1)
Deletion: O(1)
