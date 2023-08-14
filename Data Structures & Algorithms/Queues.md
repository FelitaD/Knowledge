FIFO: Like a waiting line outside a restaurant: can only add at the end (tail) and remove at the beginning (head) of the queue.

## Implementation

- SimpleQueue
- list

```python
from queue import SimpleQueue

waiting_line = SimpleQueue()

# Enqueue
waiting_line.put('Geraldine')
waiting_line.put('Martine')
waiting_line.put('Fernande')

# Count
waiting_line.qsize()
>>> 3

# Dequeue
waiting_line.get()
>>> Geraldine

# Empty
waiting_line.empty()
>>> False
```

```python
waiting_line = []

waiting_line.append('Geraldine')
waiting_line.append('Martine')
waiting_line.append('Fernande')

print(waiting_line.pop(0))
>>> Geraldine
```

## Operations & Complexity

Search: need to traverse all the nodes so O(n)
Insertion: O(1)
Deletion: O(1)
