When a problem's solution is solving the same subproblem multiple times.

Fibonacci sequence
```python
def fib(n):
	if n == 0 or n == 1:
		return n
	return fib(n-1) + fib(n-2)
```
If we call `fib(5)`:
![[Pasted image 20230622160343.png|400]]
**It recursively calls `fib(2)` three times**.