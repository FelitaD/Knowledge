`O(n²)`
Iterates through the list and selects the minimum.

```python
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        lowest = my_list[i]
        lowest_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < lowest:
                lowest_index = j
                lowest = my_list[j]
        my_list[i] , my_list[lowest_index] = my_list[lowest_index] , my_list[i]
    return my_list

```

1. Find the position **X** of the smallest item in the range of [**L**...**N**−1],
2. Swap **X**-th item with the **L**-th item,
3. Increase the lower-bound **L** by 1 and repeat Step 1 until **L** = **N**-2.