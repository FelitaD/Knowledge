Automatically free up memory that program isn't anymore using.
```python
def get_min(nums):     
	nums_sorted = sorted(nums)     
	return nums_sorted[0]  
		
my_nums = [5, 3, 1, 4, 6] 
print(get_min(my_nums))
```
`nums_sorted` is erased by the garbage collector.

The garbage collector :
1. Carefully figures out what we might still need
2. Free everything else