
Searches through a pre-sorted array by comparing middle with search value.

```python
def binary_search(ordered_list, search_value):
  first = 0
  last = len(ordered_list) - 1
  while first <= last:
    middle = (first + last)//2
    if search_value == ordered_list[middle]:
      return True
    elif search_value < ordered_list[middle]:
      last = middle - 1
    else:
      first = middle + 1
  return False
```

