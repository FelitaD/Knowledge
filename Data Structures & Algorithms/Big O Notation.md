
- **Drop constants**
`O(1 + n/2 + 100) -> O(n)`
`O(2n) -> O(n)` :
```python
def print_all_items_twice(items):     
	for item in items:         
		print(item)
	for item in items:         
		print(item)
```

- **Drop less significant terms**
`O(n + n²) -> O(n²)`
`O(n³ + 50n² + 100) -> O(n³)`

- **Usually talking about the worst case**
Sometimes difference best and worse case is high:
```python
def contains(haystack, needle):
	for item in haystack:
		if item == needle: 
			return True
	return False
```
Best case : if needle is first item -> O(1) 
Worst case: if needle is last item -> O(n)

- **Space complexity**
We're talking about the additional space, so we don't include space taken up by the inputs. 

****
![[Pasted image 20230611184235.png]]
Fastest to slowest:
1. O(**1**) - constant time 
2. O(log **n**) - logarithmic time 
3. O(**n**) - linear time 
4. O(**n** log **n**) - quasilinear time 
5. O(**n**2) - quadratic time 
6. O(**n**3) - cubic time 
7. O(2**n**) - exponential time 
8. O(**n**!) - also exponential time 
9. ∞ - infinite