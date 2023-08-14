
Like an array with arbitrary keys instead of indices.

Associates keys with values **array(key, index, value)** with the **hash technique** that generates an index based on the key.
Insertion and searches in the hash table become very quick (O(1)).

![[Pasted image 20230617125914.png|400]]
## Implementation

- dictionaries

```python
menu = {
    'entree': 'soupe miso',
    'plat': 'dahl de lentilles',
    'dessert': 'mousse au chocolat'
}

menu['plat'] = 'boeuf bourguignon'


print(menu.items())
print(menu.keys())
print(menu.values())

print(menu.get('fromage'))
print(menu['fromage'])  # raises an exception

menu.clear()
del menu
```

## Operations & Complexity

All operations:
- worst case: O(logn)
- average case: O(1)

