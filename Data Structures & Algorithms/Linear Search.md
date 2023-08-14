Iterates through a list until it finds the search value.

```python
def linear_search(unordered_list, search_value):
    for i in range(len(unordered_list)):
        if unordered_list[i] == search_value:
            return True
    return False 
```