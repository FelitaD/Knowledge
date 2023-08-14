To avoid calculating multiple times overlapping subproblems.

Common strategy for [[Dynamic Programming]] problems as well as bottom-up.

Fibonacci with memoization
```python
class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError(
                'Index was negative. '
                'No such thing as a negative index in a series.'
            )

        # Base cases
        if n in [0, 1]:
            return n

        # See if we've already calculated this
        if n in self.memo:
            print("grabbing memo[%i]" % n)
            return self.memo[n]

        print("computing fib(%i)" % n)
        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result

>>> Fibber().fib(5) 
>>> computing fib(5) 
>>> computing fib(4) 
>>> computing fib(3) 
>>> computing fib(2) 
>>> grabbing memo[2] 
>>> grabbing memo[3] 
>>> 5
```
