```python
def qsort(mylist):
    if not mylist:
        return []
    else:
        pivot = mylist[0]
        qless = qsort([x for x in mylist[1:] if x < pivot])
        qmore = qsort([x for x in mylist[1:] if x >= pivot])
        return qless + [pivot] + qmore
```