Bottom-up starts at the beginning while a recursive algorithm starts at the end.
Saves the memory cost of the call stack built up in recursion.

Top-down (with stack overflow risk) -> `O(n)` space
```python
def product_1_to_n(n):
	return n * product_1_to_n(n-1) if n > 1 else 1
```

Bottom-up -> `O(1)` space
```python
def product_1_to_n(n):
	result = 1
	for num in range(1, n+1):
		result *= num
	return result
```