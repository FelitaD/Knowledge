`O(n²)`
```python
def bubble_sort(my_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True # will be evaluated in the while after loop exits
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]: # while the loop is not in ascending order
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                print(my_list)
                is_sorted = False # the loop will continue
    return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))
```

1. **Compare** a pair of adjacent items (a, b),
2. Swap that pair if the items are out of order (in this case, when a > b),
3. Repeat Step 1 and 2 until we reach the end of array
    (the last pair is the (**N**-2)-th and (**N**-1)-th items as we use 0-based indexing),
4. By now, the largest item will be at the last position.
    We then reduce **N** by 1 and repeat Step 1 until we have **N = 1**.
